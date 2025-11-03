from datasets import load_dataset


def download_dataset():
    dataset = load_dataset('shuttie/dadjokes')

    dataset['train'].to_csv('src/data/raw/train_raw.csv')
    dataset['test'].to_csv('src/data/raw/test_raw.csv')

    return 'Raw Datasets downloaded !\n'