from datasets import load_dataset
from pathlib import Path


def download_dataset():
    dataset = load_dataset('shuttie/dadjokes')

    Path('src/data/raw').mkdir(parents=True, exist_ok=True)

    dataset['train'].to_csv('src/data/raw/train_raw.csv')
    dataset['test'].to_csv('src/data/raw/test_raw.csv')

    return 'Raw Datasets downloaded !\n'