# This script converts the two train and test dataset into one single parent dataset.


from config.paths import RAW_SET_DIR, MERGED_SET_DIR
from src.utils.dataset_loader import read_dataset


def merge_dataset():
    train = read_dataset(RAW_SET_DIR + '/train_raw.csv', 'csv')
    test = read_dataset(RAW_SET_DIR + '/test_raw.csv', 'csv')

    dataset = train.vstack(test)
    print(dataset.head())

    dataset.write_csv(MERGED_SET_DIR + '/dad_jokes.csv')

    return 'Full Dataset saved !\n'