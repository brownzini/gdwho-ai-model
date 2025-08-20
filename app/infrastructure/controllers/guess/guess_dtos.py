from app.infrastructure.handlers.exceptions.GuessException import GuessException
from app.infrastructure.handlers.global_handler import raise_http_error

from pydantic import BaseModel
from typing import List

class GuessRequest(BaseModel):
    data: List[str]
    input: str
    id: int

def field_validation(fieldName:str, fieldSize:int, min:int, max:int):
    if fieldSize >= min and fieldSize <= max:
        return ""
    else:
        return GuessException.getDefaultMessage(fieldName)

def guess_request_dto(request:GuessRequest):
    
    inputSize = len(request.input.strip())
    dataSize = len(request.data)
    
    input = field_validation("input", inputSize, 3, 100)
    data  = field_validation("data", dataSize, 1, 100)
    
    message_error = input+data

    if input != "" or data != "":
       raise raise_http_error(status_code=400, message=message_error) 
   
    return request