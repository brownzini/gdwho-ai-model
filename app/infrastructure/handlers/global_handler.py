from fastapi import HTTPException
from typing import Any

def raise_http_error(status_code: int = 500, message: str = "Internal Server Error") -> Any:
    raise HTTPException(status_code=status_code, detail=message)