from abc import ABC, abstractmethod
from sentence_transformers import InputExample

class AnalyzeGateway(ABC):

    @abstractmethod
    def route_action(type:str, model_id: int, threshold: float):
        pass