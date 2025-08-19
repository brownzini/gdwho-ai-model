from app.applications.gateways.guess_gateway import GuessGateway

class GuessUsecase:
    
    def __init__(self, guess_gateway: GuessGateway):
        self.guess_gateway = guess_gateway
        
    def predict_similarity(self, model_id: int, input_text: str, data: list):
        return self.guess_gateway.predict_similarity(model_id, input_text, data)
