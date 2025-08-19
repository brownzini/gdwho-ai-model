from fastapi import APIRouter, HTTPException, Depends

from app.applications.usecases.guess_usecase import GuessUsecase
from app.infrastructure.gateways.guess.guess_impl import GuessImplementation
from app.model.schemas import GuessRequest

router = APIRouter()

def get_guess_usecase() -> GuessUsecase:
    guess_impl = GuessImplementation()
    return GuessUsecase(guess_impl)

@router.post("")
def guess(request: GuessRequest):
    if not request.input.strip():
        return {"error": "empty input"}
    if not request.data:
        return {"error": "empty data"}
    try:
        guess_impl = GuessImplementation()
        guess_usecase = GuessUsecase(guess_impl)
        return guess_usecase.predict_similarity(request.id, request.input, request.data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))