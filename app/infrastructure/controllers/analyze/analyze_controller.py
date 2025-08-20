from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.gateways.analyze.analyze_impl import route_action

router = APIRouter()

@router.get("")
async def analyze(id: int, type: str):
    try:
        return { route_action(type, id, [], 3) }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))