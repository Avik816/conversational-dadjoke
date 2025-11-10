# This script converts the two train and test dataset into one single parent dataset.


from src.utils.dataset_loader import read_dataset
from config.paths import RAW_SET_DIR, MERGED_SET_DIR
from config.file_names import TRAIN, TEST, TYPE1, FULL_FILE


def merge_dataset():
    train = read_dataset(f'{RAW_SET_DIR}/{TRAIN}', TYPE1)
    test = read_dataset(f'{RAW_SET_DIR}/{TEST}', TYPE1)

    dataset = train.vstack(test)
    print(dataset.head())

    dataset.write_csv(f'{MERGED_SET_DIR}/{FULL_FILE}')

    return 'Full Dataset saved !\n'