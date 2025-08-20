import numpy as np

from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
from sklearn.decomposition import PCA

from app.applications.gateways.analyze_gateway import AnalyzeGateway
from app.config.model_config import get_model
from app.domain.domain_constants import DATA_CROSS_MODEL_NAME_PREFIX, DATA_ERRORS_MODEL_NAME_PREFIX, GRAPHS_MODEL_NAME_PREFIX
from app.infrastructure.data_loader.loader import load_csv_as_input_examples
from pathlib import Path

from sklearn.model_selection import KFold
from sentence_transformers import InputExample, losses
from torch.utils.data import DataLoader

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
        plt.xlabel("[Distância]")
        plt.ylabel("[Progressão]")

        buf = BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        
        return StreamingResponse(buf, media_type="image/png")

    def analyze_validation_cross_model_csv(self, model_id):

        k = 5
        epochs = 1 
        batch_size = 8

        csv_name = f"data/cross/{DATA_CROSS_MODEL_NAME_PREFIX}{model_id}.csv"
        csv_path = Path(__file__).parent.parent.parent / csv_name
        
        entries = load_csv_as_input_examples(csv_path)

        if len(entries) == 0:
            raise ValueError(f"CSV is empty or did not load data: {csv_path}")

        n_splits = min(k, len(entries))
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

        fold_results = []

        for fold, (train_idx, test_idx) in enumerate(kf.split(entries), 1):

            train_data = [entries[i] for i in train_idx]
            test_data = [entries[i] for i in test_idx]

            model = get_model(model_id)

            train_examples = [
                InputExample(texts=[ex.texts[0], ex.texts[1]], label=ex.label)
                for ex in train_data
            ]
            train_loader = DataLoader(train_examples, shuffle=True, batch_size=batch_size)
            train_loss = losses.CosineSimilarityLoss(model)

            model.fit(train_objectives=[(train_loader, train_loss)], epochs=epochs)

            sim_sum = 0
            for ex in test_data:
                emb1 = model.encode(ex.texts[0])
                emb2 = model.encode(ex.texts[1])
                sim = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
                sim_sum += abs(sim - ex.label)

            avg_error = sim_sum / len(test_data)
            fold_results.append(avg_error)

        fold_results = [float(x) for x in fold_results]
        return fold_results
        
    def route_action(self, type:str, model_id: int, threshold: float):
        if(type == "errors"): return self.analyze_model_errors_from_csv(model_id, threshold)
        if(type == "graphs"): return self.analyze_modeL_graphs_from_csv(model_id)
        if(type == "validation"): return self.analyze_validation_cross_model_csv(model_id)
        return {"[ERROR]": "Invalid type"}