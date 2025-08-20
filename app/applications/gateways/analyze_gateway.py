from abc import ABC, abstractmethod
from sentence_transformers import InputExample

class AnalyzeGateway(ABC):

    @abstractmethod
    def analyze_model_errors(model_id: int, val_data: list[InputExample], threshold: float):
        pass