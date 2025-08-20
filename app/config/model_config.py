from sentence_transformers import SentenceTransformer
from functools import lru_cache

from app.domain.domain_constants import MODEL_NAME_PREFIX

@lru_cache(maxsize=16)
def get_model(model_id: int) -> SentenceTransformer:
    return SentenceTransformer(f"{MODEL_NAME_PREFIX}{model_id}")