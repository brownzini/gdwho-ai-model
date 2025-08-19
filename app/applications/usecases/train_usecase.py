from app.applications.gateways.train_gateway import TrainGateway

class TrainUsecase:
    
    def __init__(self, train_gateway: TrainGateway):
        self.train_gateway = train_gateway
        
    def get_model(self, model_id: int) -> str:
        return self.train_gateway.get_model(model_id)
