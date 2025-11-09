# This script creates the necessary directories for this project.


from config.paths import *
from pathlib import Path
import os


def create_dirs():
    if not os.path.exists(RAW_SET_DIR):
        Path('data/raw').mkdir(parents=True, exist_ok=True)
    if not os.path.exists(MERGED_SET_DIR):
        Path('data/merged').mkdir(parents=True, exist_ok=True)
    if not os.path.exists(FINAL_SET_DIR):
        Path('data/cleaned').mkdir(parents=True, exist_ok=True)
    if not os.path.exists(MODEL_DIR):
        Path('models/embedder').mkdir(parents=True, exist_ok=True)
    if not os.path.exists(EMBEDDED_SET_DIR):
        Path('db/vector_embedds').mkdir(parents=True, exist_ok=True)

    return 'Necessary Directories created.\n'