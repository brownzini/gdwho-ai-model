from app.applications.gateways.train_gateway import TrainGateway

class TrainImplementation(TrainGateway):
    
    def get_model(self, model_id: int) -> str:
        return f"Modelo {model_id} carregado"
