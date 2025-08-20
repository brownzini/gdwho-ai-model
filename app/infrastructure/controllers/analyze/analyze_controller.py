from fastapi import APIRouter, Depends, HTTPException

from app.applications.usecases.analyze_usecase import AnalyzeUsecase
from app.infrastructure.gateways.analyze.analyze_impl import AnalyzeImplementation

router = APIRouter()

def get_analyze_usecase() -> AnalyzeUsecase:
    analyze_impl = AnalyzeImplementation()
    return AnalyzeUsecase(analyze_impl)

@router.get("")
async def analyze(
    id: int, 
    type: str,
    analyze_usecase: AnalyzeUsecase = Depends(get_analyze_usecase)
):
    try:
        return analyze_usecase.route_action(type, id, 3)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))