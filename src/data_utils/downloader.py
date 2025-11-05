# This scripts download the dataset from Hugging Face Datasets.
# It originally downloads in arrow format and splitted as train and tests.
# This scripts converts the dataset from the said format to .csv.

from datasets import load_dataset
from pathlib import Path


def download_dataset():
    dataset = load_dataset('shuttie/dadjokes')

    Path('data/raw').mkdir(parents=True, exist_ok=True)

    dataset['train'].to_csv('data/raw/train_raw.csv')
    dataset['test'].to_csv('data/raw/test_raw.csv')

    return 'Raw Datasets downloaded !\n'