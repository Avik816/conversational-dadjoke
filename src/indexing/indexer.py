from ..utils.dataset_loader import read_dataset
from ..config.paths import EMBEDDED_SET_DIR, INDEX_SET_DIR
from ..config.file_names import EMBEDDED_SET, TYPE2, INDEX_SET, ID_MAP_SET
import faiss
import numpy
import polars


def generate_faiss_index():
    dataset = read_dataset(f'{EMBEDDED_SET_DIR}/{EMBEDDED_SET}', TYPE2)

    # Converting embeddings to NumPy float32 array
    embeddings = numpy.array(dataset['embedding'].to_list()).astype('float32')

    # Get joke IDs in the same order
    joke_ids = dataset['joke_id'].to_list()

    # Build FAISS index (Inner Product works as cosine if normalized)
    dim = embeddings.shape[1]
    print(f'Building FAISS index with dimension: {dim}\n')

    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    print(f'Total vectors added: {index.ntotal}\n')

    # Saving FAISS index
    faiss.write_index(index, f'{INDEX_SET_DIR}/{INDEX_SET}')

    # Saving joke_id with FAISS position mapping
    id_map = polars.DataFrame({
        'joke_id': joke_ids,
        'faiss_index': list(range(len(joke_ids)))        
    })
    id_map.write_parquet(f'{INDEX_SET_DIR}/{ID_MAP_SET}')

    print('FAISS index and ID mapping saved successfully.\n')