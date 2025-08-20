from typing import List
from app.applications.usecases.train_usecase import TrainUsecase
from app.domain.entry_domain import EntryDomain
from app.infrastructure.gateways.train.train_impl import TrainImplementation

def test_get_model():
    
    train_impl = TrainImplementation()
    usecase = TrainUsecase(train_impl)

    raw_entries = [
        {"input": "input1", "output": "output1", "label": 0.5},
        {"input": "input2", "output": "output2", "label": 1.0},
    ]

    model_id = 1
    epochs = 3
    batch_size = 4
    warmup_steps = 10
    
    result = usecase.train_model(model_id, raw_entries, epochs, batch_size, warmup_steps)
    assert isinstance(result, str) 
