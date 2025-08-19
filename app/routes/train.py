from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("")
def train():
    try:
        print("initiate train")
        return {"message": f"success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
