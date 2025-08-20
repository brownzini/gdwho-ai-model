from app.applications.gateways.guess_gateway import GuessGateway
from app.config.model_config import get_model
import torch

class GuessImplementation(GuessGateway):
    
    def predict_similarity(self, model_id: int, input_text: str, data: list):
        model = get_model(model_id)
        texts = [input_text.strip()] + data
        embeddings = model.encode(texts, convert_to_tensor=True, normalize_embeddings=True)
        user_emb = embeddings[0]
        data_embs = embeddings[1:]
        sims = torch.matmul(user_emb, data_embs.T)
        idx = int(torch.argmax(sims).item())
        score = float(sims[idx])
        return { "result": round(score, 4) }

    
