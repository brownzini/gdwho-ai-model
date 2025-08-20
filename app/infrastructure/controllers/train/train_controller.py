from fastapi import APIRouter, HTTPException, Depends
from app.applications.usecases.train_usecase import TrainUsecase
from app.infrastructure.controllers.train.train_dtos import TrainRequest, train_request_dto
from app.infrastructure.gateways.train.train_impl import TrainImplementation

router = APIRouter()

def get_train_usecase() -> TrainUsecase:
    train_impl = TrainImplementation()
    return TrainUsecase(train_impl)

@router.post("")
def train(
    request: TrainRequest = Depends(train_request_dto),
    train_usecase: TrainUsecase = Depends(get_train_usecase)
):
    epochs = 3
    batch_size = 4
    warmup_steps = 10
    try:
        return train_usecase.train_model(request.id, request.entries, epochs, batch_size, warmup_steps)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
