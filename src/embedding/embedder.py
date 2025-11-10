# This script is used to generate the embeddings for the dataset.


from config.paths import FINAL_SET_DIR, EMBEDDED_SET_DIR
from config.file_names import FULL_FILE, TYPE1, EMBEDDED_SET, JOKE_EMBEDDINGS
from utils.dataset_loader import read_dataset
import polars
from utils.model_loader import load_model
import numpy


def generate_embeddings():
    # Loading the dataset
    dataset = read_dataset(f'{FINAL_SET_DIR}/{FULL_FILE}', TYPE1)

    # Combining setup + response into a single text field for embedding.
    dataset = dataset.with_columns((
        polars.col('question').str.strip() + ' ' +
        polars.col('response').str.strip()
        ).alias('joke_text')
    )

    # Loading embedding model to a custom directory.
    model = load_model()

    # Generating embeddings for the combined text.
    jokes_texts = dataset['joke_texts'].to_list()
    embeddings = model.encode(jokes_texts, normalize_embeddings=True)

    # Adding embeddings as a new column.
    dataset = dataset.with_columns(
        polars.Series('embedding', [e.tolist() for e in embeddings])
    )

    # Saving the dataset with embeddings.
    dataset.write_parquet(f'{EMBEDDED_SET_DIR}/{EMBEDDED_SET}')

    # Saving just the embeddings separately for FAISS use.
    numpy.save(f'{EMBEDDED_SET_DIR}/{JOKE_EMBEDDINGS}', embeddings)

    return 'Embeddings generated and saved successfully.\n'