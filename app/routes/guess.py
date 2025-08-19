from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("")
def guess():
    try:
        return {"message": f"guess success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))