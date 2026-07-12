from functools import lru_cache
import pickle
from pathlib import Path

from langchain_core.documents import Document

SAVE_PATH = Path("data/processed/indexed_chunks.pkl")


class DocumentStorage:

    @staticmethod
    def save(documents: list[Document]) -> None:

        SAVE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(SAVE_PATH, "wb") as f:
            pickle.dump(documents, f)

        # Clear cache after saving new data
        DocumentStorage.load.cache_clear()


    @staticmethod
    @lru_cache(maxsize=1)
    def load() -> list[Document]:

        with open(SAVE_PATH, "rb") as f:
            return pickle.load(f)