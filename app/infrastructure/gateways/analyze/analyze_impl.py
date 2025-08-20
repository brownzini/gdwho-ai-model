from sentence_transformers import SentenceTransformer, InputExample
import numpy as np

from app.config.teste import get_model
from app.domain.domain_constants import BASE_MODEL_NAME

def analyze_model_errors(model_id: int, val_data: list[InputExample], threshold: float = 0.3):        
    return "funciona kkkkk"

def route_action(type:str, model_id: int, val_data: list[InputExample], threshold: float):
    # if(type == "errors"): analyze_model_errors(model_id, val_data, threshold)
    return "salve kkkkk"