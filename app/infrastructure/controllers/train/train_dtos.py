from pydantic import BaseModel
from typing import List

from app.domain.entry_domain import EntryDomain

from app.infrastructure.handlers.exceptions.TrainException import TrainException
from app.infrastructure.handlers.global_handler import raise_http_error

class TrainRequest(BaseModel):
    id: int
    entries: List[EntryDomain]

def field_validation(fieldName:str, fieldSize:int, min:int, max:int):
    if fieldSize >= min and fieldSize <= max:
        return ""
    else:
        return TrainException.getDefaultMessage(fieldName)

def train_request_dto(request:TrainRequest):
    
    entriesSize = len(request.entries)
    message_error = field_validation("entries", entriesSize, 3, 100)
    
    if message_error != "":
        raise raise_http_error(status_code=400, message=message_error) 

    return request