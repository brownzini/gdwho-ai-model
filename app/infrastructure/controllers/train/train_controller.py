from fastapi import APIRouter, HTTPException, Depends
from app.applications.usecases.train_usecase import TrainUsecase
from app.infrastructure.controllers.train.train_dto import TrainingRequest
from app.infrastructure.gateways.train.train_impl import TrainImplementation

router = APIRouter()

def get_train_usecase() -> TrainUsecase:
    train_impl = TrainImplementation()
    return TrainUsecase(train_impl)

@router.post("")
def train(
    request: TrainingRequest,
    train_usecase: TrainUsecase = Depends(get_train_usecase)
):
    try:
        return train_usecase.train_model(request.id, request.entries, 3,4,10)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
