# This scrpts loads the embedder model


from sentence_transformers import SentenceTransformer
from config.paths import MODEL_DIR

def load_model():
    model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder=MODEL_DIR)

    return model