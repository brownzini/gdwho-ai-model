import numpy as np

from app.applications.gateways.analyze_gateway import AnalyzeGateway
from app.config.teste import get_model
from app.domain.domain_constants import DATA_ERRORS_MODEL_NAME_PREFIX
from app.infrastructure.data_loader.loader import load_csv_as_input_examples
from pathlib import Path

class AnalyzeImplementation(AnalyzeGateway):

    def analyze_model_errors_from_csv(self, model_id: int, csv_path: str, threshold: float = 0.3):

        model = get_model(model_id)
        csv_name = f"data/errors/{DATA_ERRORS_MODEL_NAME_PREFIX}{model_id}.csv"

        csv_path = Path(__file__).parent.parent.parent / csv_name

        val_data = load_csv_as_input_examples(csv_path)
        errors = []
        
        for ex in val_data:
            emb1 = model.encode(ex.texts[0])
            emb2 = model.encode(ex.texts[1])
            sim = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
            diff = abs(sim - ex.label)

            if diff > threshold:
                errors.append({
                    "texts": ex.texts,
                    "label": ex.label,
                    "predicted": float(sim),
                    "error": float(diff)
                })

        errors.sort(key=lambda x: x["error"], reverse=True)
        return errors
    
    def route_action(self, type:str, model_id: int, threshold: float):
        if(type == "errors"): return self.analyze_model_errors_from_csv(model_id, threshold)
        return "salve kkkkk"