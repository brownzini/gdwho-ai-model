from app.applications.gateways.analyze_gateway import AnalyzeGateway
from sentence_transformers import InputExample

class AnalyzeUsecase:
    
    def __init__(self, analyze_gateway: AnalyzeGateway):
        self.analyze_gateway = analyze_gateway
        
    def route_action(self, type:str, model_id: int, threshold: float):
        return self.analyze_gateway.route_action(type, model_id, threshold)
