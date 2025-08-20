from typing import List
from sentence_transformers import SentenceTransformer, losses, InputExample
from torch.utils.data import DataLoader
from sentence_transformers import SentenceTransformer
from app.applications.gateways.train_gateway import TrainGateway
from app.config.teste import get_model
from app.domain.domain_constants import BASE_MODEL_NAME, MODEL_NAME_PREFIX
from app.domain.entry_domain import EntryDomain

class TrainImplementation(TrainGateway):

    def train_model(self, id: int, entries:List[EntryDomain], epochs:int=3, batch_size:int=5, warmup_steps:int=10) -> bool:
   
        model = SentenceTransformer(BASE_MODEL_NAME)
        input_data = [
            InputExample(texts=[ex.input, ex.output], label=ex.label)
            for ex in entries
        ]

        dataloader = DataLoader(input_data, shuffle=True, batch_size=batch_size)
        train_loss = losses.CosineSimilarityLoss(model=model)

        model.fit(
            train_objectives=[(dataloader, train_loss)],
            epochs=epochs,
            warmup_steps=warmup_steps,
            show_progress_bar=True
        )

        model_path = f"{MODEL_NAME_PREFIX}{id}"
        model.save(model_path)

        get_model.cache_clear()
        
        return True

