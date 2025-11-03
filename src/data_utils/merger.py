import polars
from pathlib import Path


def merge_dataset():
    train = polars.read_csv('src/data/raw/train_raw.csv')
    test = polars.read_csv('src/data/raw/test_raw.csv')

    dataset = train.vstack(test)

    print(dataset.head())

    Path('src/data/merged').mkdir(parents=True, exist_ok=True)

    dataset.write_csv('src/data/merged/dad_jokes.csv')

    return 'Full Dataset saved !\n'