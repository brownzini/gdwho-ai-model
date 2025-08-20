from app.applications.gateways.analyze_gateway import AnalyzeGateway
from sentence_transformers import InputExample

class AnalyzeUsecase:
    
    def __init__(self, analyze_gateway: AnalyzeGateway):
        self.analyze_gateway = analyze_gateway
        
    def analyze_model_errors(self, model_id: int, val_data: list[InputExample], threshold: float):
        return self.analyze_gateway.analyze_model_errors(model_id, val_data, threshold)
