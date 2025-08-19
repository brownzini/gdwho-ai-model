from abc import ABC, abstractmethod

class GuessGateway(ABC):

    @abstractmethod
    def predict_similarity(model_id: int, input_text: str, data: list): 
        pass
