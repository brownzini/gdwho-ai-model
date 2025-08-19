from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("")
def train():
    try:
        return {"message": f"train success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
