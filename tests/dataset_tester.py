# This script tests the dataset's schematic order.


import polars, faiss


dataset = polars.read_parquet('db/vector_embedds/dadjoke_embedded.parquet')
# print(dataset.head(1))

del dataset

dataset = polars.read_parquet('db/vector_index/faiss_id_map.parquet')
# print(dataset.head())

# Load the index
index = faiss.read_index("db/vector_index/dadjoke_faiss.index")
print(index)

# Check how many vectors are in it
print("Number of vectors:", index.ntotal)