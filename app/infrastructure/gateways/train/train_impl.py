from typing import List
from app.applications.gateways.train_gateway import TrainGateway
from app.domain.entry_domain import EntryDomain

class TrainImplementation(TrainGateway):
    
    def train_model(self, id: int, entries:List[EntryDomain], epochs:int=3, batch_size:int=5, warmup_steps:int=10) -> bool:
        return True
