from fastapi import APIRouter, HTTPException

from app.model.schemas import TrainingRequest
from app.services.model_service import get_model

router = APIRouter()

@router.post("")
def train(request: TrainingRequest):
    try:
        return get_model(request.id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
