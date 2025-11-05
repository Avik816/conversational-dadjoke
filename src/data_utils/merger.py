# This script converts the two train and test dataset into one single parent dataset.


import polars
from pathlib import Path


def merge_dataset():
    train = polars.read_csv('data/raw/train_raw.csv')
    test = polars.read_csv('data/raw/test_raw.csv')

    dataset = train.vstack(test)

    print(dataset.head())

    Path('data/merged').mkdir(parents=True, exist_ok=True)

    dataset.write_csv('data/merged/dad_jokes.csv')

    return 'Full Dataset saved !\n'