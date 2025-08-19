from pydantic import BaseModel
from typing import List

class EntryBase(BaseModel):
    input: str
    output: str
    label: float

class TrainingRequest(BaseModel):
    id: int
    entries: List[EntryBase]

class GuessRequest(BaseModel):
    data: List[str]
    input: str
    id: int
