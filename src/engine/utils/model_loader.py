# This script loads the embedder model.


from sentence_transformers import SentenceTransformer
from ..config.file_names import EMBEDDER_MODEL
from ..config.paths import MODEL_DIR


def load_model():
    model = SentenceTransformer(EMBEDDER_MODEL, cache_folder=MODEL_DIR)

    return model