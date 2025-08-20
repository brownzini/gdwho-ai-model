from typing import List
from app.applications.gateways.train_gateway import TrainGateway
from app.domain.entry_domain import EntryDomain

class TrainUsecase:
    
    def __init__(self, train_gateway: TrainGateway):
        self.train_gateway = train_gateway
        
    def train_model(self, id: int, entries:List[EntryDomain], epochs:int, batch_size:int, warmup_steps:int) -> bool:
        return self.train_gateway.train_model(id, entries, epochs, batch_size, warmup_steps)
