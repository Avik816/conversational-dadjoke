# This scripts download the dataset from Hugging Face Datasets.
# It originally downloads in arrow format and splitted as train and tests.
# This scripts converts the dataset from the said format to .csv.

from datasets import load_dataset
from config.paths import HF_DADJOKE_LOC, RAW_SET_DIR
from config.file_names import TRAIN, TEST


def download_dataset():
    dataset = load_dataset(HF_DADJOKE_LOC)

    dataset['train'].to_csv(f'{RAW_SET_DIR}/{TRAIN}')
    dataset['test'].to_csv(f'{RAW_SET_DIR}/{TEST}')

    return 'Raw Datasets downloaded !\n'