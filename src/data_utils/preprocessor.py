'''
This script preprocesses the raw full csv files.
It clears the data from any of the folllowing:
    1. URLs.
    2. Any kind of HTML entries.
    3. Any kind of redundant square brackets.
    4. Changing the quations from curly quotes to UTF-8 encoded quotes.
    5. Removing emojis if there was any.
    6. Removing any reddit based patterns whent he jokes were originally scrapped.
    7. Removing any rows that had questions of length < 5 (according to string length).
'''


from src.utils.dataset_loader import read_dataset
from config.paths import MERGED_SET_DIR, FINAL_SET_DIR
from config.file_names import FULL_FILE, TYPE1
import re
import polars


def checking_for_url(text):
    url_pattern = re.compile(r'https?://|www\.|\.com|\.net|\.org|\.io|\.gov|\.in|\.me|\.co', re.IGNORECASE)

    return bool(url_pattern.search(str(text)))

def checking_for_html_entities(text):
    html_entity_pattern = re.compile(r"&(gt|lt|amp|quot|apos);", re.IGNORECASE)

    return bool(html_entity_pattern.search(str(text)))

def checking_for_square_brackets(text):
    return bool(re.search(r"\[|\]", str(text)))

def deleting_quotes(text):
    return (
        text.replace('“', '"').replace('”', '"').
        replace('‘', "'").replace('’', "'")
    )

def removing_emojis(text):    
    emoji_pattern = re.compile(
        r"["
        "\U0001F600-\U0001F64F"  # Emoticons (😀–😿)
        "\U0001F300-\U0001F5FF"  # Symbols & pictographs
        "\U0001F680-\U0001F6FF"  # Transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # Regional flags
        "\U00002500-\U00002BEF"  # Chinese/Japanese/Korean
        "\U00002700-\U000027BF"  # Dingbats
        "\U0001F900-\U0001F9FF"  # Supplemental symbols
        "\U0001FA70-\U0001FAFF"  # Extended pictographs
        "\U000024C2-\U0001F251"  # Enclosed characters
        "\uFF00-\uFFEF"          # Full-width ASCII variants
        "\u2600-\u26FF"          # Misc symbols
        "\u2000-\u206F"          # General punctuation
        "\u00A0-\u00FF"          # Latin-1 Supplement
        "\u0100-\u017F"          # Latin Extended-A
        "\u0180-\u024F"          # Latin Extended-B
        "]+", flags=re.UNICODE
    )
    
    return emoji_pattern.sub('', str(text))

def removing_kaoemoji_patterns(text):
    kaomoji_face_pattern = re.compile(r"\([\s\S]{3,20}?\)")

    return kaomoji_face_pattern.sub('', str(text))

def removing_reddit_pattern(text): # Other noises
    reddit_pattern = re.compile(r"(\/r\/\w+|u\/\w+|post:)", re.IGNORECASE)

    return reddit_pattern.sub('', str(text))

def cleaning_text(text):
    text = str(text).strip()
    text = deleting_quotes(text)
    text = removing_emojis(text)
    text = removing_kaoemoji_patterns(text)
    text = removing_reddit_pattern(text)
    text = re.sub(r'\s+', ' ', text)

    return text

# Applying the custom functions on the dataset
def preprocess_dataset():
    dataset = read_dataset(f'{MERGED_SET_DIR}/{FULL_FILE}', TYPE1)
    print(f'Original Shape: {dataset.shape}')

    # Checking and removing rows with NaN and Null values
    print('\nNull Count ...\n', dataset.null_count())
    dataset = dataset.drop_nulls().drop_nulls()
    print(f'After Null and NaN removal, Dataset Shape: {dataset.shape}')

    # Checking and removing duplicated values
    print(f'\nDataset is Duplicated ?: {dataset.is_duplicated().any()}')
    dataset = dataset.unique()
    print(f'After duplicate value removal, Dataset Shape: {dataset.shape}')
    
    # Filtering out URLs
    dataset = dataset.filter(~dataset.map_rows(checking_for_url).to_series())
    print(f'\nAfter filterign out URLs, Dataset Shape: {dataset.shape}')

    # Filtering out HTML Entries
    dataset = dataset.filter(~dataset.map_rows(checking_for_html_entities).to_series())
    print(f'\nAfter filterign out HTML entries, Dataset Shape: {dataset.shape}')

    # Filtering out Square Brackets
    dataset = dataset.filter(~dataset.map_rows(checking_for_square_brackets).to_series())
    print(f'\nAfter filterign out Square brackets, Dataset Shape: {dataset.shape}')

    # Deleting quotes, emojis and reddit patterns
    dataset = dataset.with_columns(
        (
            polars.col('question').
            map_elements(
                function=lambda t: cleaning_text(t),
                return_dtype=polars.Utf8
            ).alias('question')
        ),
        (
            polars.col('response').
            map_elements(
                function=lambda t: cleaning_text(t),
                return_dtype=polars.Utf8
            ).alias('response')
        )
    )

    # Filtering out texts with small length
    # NOT considering text with length <= 5 as joke setup questions
    dataset = dataset.filter(~(polars.col('question').len().is_between(1, 5, 'both')))
    print(f'\nAfter filterign out short texts, Dataset Shape: {dataset.shape}')

    # Adding ids to each joke
    print('\nAdding columns')
    dataset = dataset.with_columns((
        polars.lit('jk_') + polars.arange(
            start=1, end=dataset.height + 1, step=1
        ).cast(polars.Utf8)).alias('joke_id')
    )
    # Reordering so joke_id is first
    dataset = dataset.select(['joke_id'] + [c for c in dataset.columns if c != 'joke_id'])

    print('\nFinal dataset after cleaning ... \n')
    print(dataset.head())

    dataset.write_csv(f'{FINAL_SET_DIR}/{FULL_FILE}')
    print('Cleaned dataset saved !')