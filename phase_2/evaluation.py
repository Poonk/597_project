import os

from config import SAVED_FIGS_DIR


def ensure_figs_dir(path=SAVED_FIGS_DIR):
    os.makedirs(path, exist_ok=True)
    return path
