from abc import ABC, abstractmethod

class TrainGateway(ABC):

    @abstractmethod
    def get_model(self, model_id:int) -> str: 
        pass
