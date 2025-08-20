from abc import ABC, abstractmethod
from typing import List

from app.domain.entry_domain import EntryDomain

class TrainGateway(ABC):

    @abstractmethod
    def train_model(id: int, entries:List[EntryDomain], epochs:int, batch_size:int, warmup_steps:int) -> bool:
        pass
