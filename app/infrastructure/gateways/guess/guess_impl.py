from app.applications.gateways.guess_gateway import GuessGateway

class GuessImplementation(GuessGateway):
    
    def predict_similarity(self, model_id: int, input_text: str, data: list):
        return { "result": round(10.40, 4) }
