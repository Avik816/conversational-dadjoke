import polars
from sentence_transformers import SentenceTransformer
import numpy
import os


def generate_embeddings():
    # Loading the dataset
    dataset = polars.read_csv('data/cleaned/dad_jokes.csv')

    # Combining setup + response into a single text field for embedding
    dataset = dataset.with_columns(
        (polars.col('setup').str.strip() + ' ' + polars.col('response').str.strip()).alias('joke_text')
    )

    # Loading embedding model to a custom directory
    model_dir = 'models/embedder/all-MiniLM-L6-v2'
    os.makedirs(model_dir, exist_ok=True)
    model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder=model_dir)

    # Generating embeddings for the combined text
    jokes_texts = dataset['joke_text'].to_list()
    embeddings = model.encode(jokes_texts, normalize_embeddings=True)

    # Adding embeddings as a new column
    dataset = dataset.with_columns(
        polars.Series('embedding', [e.tolist() for e in embeddings])
    )

    # Saving the dataset with embeddings
    os.makedirs('data/processed', exist_ok=True)
    dataset.write_parquet('data/processed/jokes_with_embeddings.parquet')

    # Save just the embeddings separately (for FAISS use)
    numpy.save('data/processed/joke_embeddings.npy', embeddings)

    return 'Embeddings generated and saved successfully.\n'