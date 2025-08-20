import numpy as np

from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
from sklearn.decomposition import PCA

from app.applications.gateways.analyze_gateway import AnalyzeGateway
from app.config.teste import get_model
from app.domain.domain_constants import DATA_ERRORS_MODEL_NAME_PREFIX, GRAPHS_MODEL_NAME_PREFIX
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

    def analyze_modeL_graphs_from_csv(self, model_id):
        
        model = get_model(model_id)

        csv_name = f"data/graphs/{GRAPHS_MODEL_NAME_PREFIX}{model_id}.csv"
        csv_path = Path(__file__).parent.parent.parent / csv_name
        
        df = pd.read_csv(csv_path)

        texts = df['input'].tolist()
        embeddings = model.encode(texts)

        pca = PCA(n_components=2)
        embeddings_2d = pca.fit_transform(embeddings)

        plt.figure(figsize=(8,6))
        plt.scatter(embeddings_2d[:,0], embeddings_2d[:,1])
        for i, txt in enumerate(texts):
            plt.annotate(txt, (embeddings_2d[i,0], embeddings_2d[i,1]), fontsize=8, alpha=0.7)
        plt.title("Visualização 2D dos embeddings do modelo")
        plt.xlabel("[Progressão]")
        plt.ylabel("[Distância]")

        buf = BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        
        return StreamingResponse(buf, media_type="image/png")
    
    def route_action(self, type:str, model_id: int, threshold: float):
        if(type == "errors"): return self.analyze_model_errors_from_csv(model_id, threshold)
        if(type == "graphs"): return self.analyze_modeL_graphs_from_csv(model_id)
        return {"[ERROR]": "Invalid type"}