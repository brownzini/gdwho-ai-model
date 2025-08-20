from fastapi import APIRouter, Depends, HTTPException

from app.applications.usecases.guess_usecase import GuessUsecase
from app.infrastructure.controllers.guess.guess_dtos import GuessRequest, request_dto
from app.infrastructure.gateways.guess.guess_impl import GuessImplementation

router = APIRouter()

def get_guess_usecase() -> GuessUsecase:
    guess_impl = GuessImplementation()
    return GuessUsecase(guess_impl)

@router.post("")
def guess(
    request: GuessRequest = Depends(request_dto), 
    guess_usecase: GuessUsecase = Depends(get_guess_usecase)
):
    try:
        return guess_usecase.predict_similarity(request.id, request.input, request.data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))