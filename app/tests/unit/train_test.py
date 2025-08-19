from app.applications.usecases.train_usecase import TrainUsecase
from app.infrastructure.gateways.train.train_impl import TrainImplementation

def test_get_model():
    train_impl = TrainImplementation()
    usecase = TrainUsecase(train_impl)
    
    result = usecase.get_model(1)
    assert isinstance(result, str) 
