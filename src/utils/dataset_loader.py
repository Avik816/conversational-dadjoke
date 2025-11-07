# This script is used to load the different dataset used.


import polars


def read_dataset(path, type):
    if type == 'csv':
        dataset = polars.read_csv(path)
    if type == 'parquet':
        dataset = polars.read_parquet(path)

    return dataset