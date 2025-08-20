from pydantic import BaseModel

class EntryBase(BaseModel):
    input: str
    output: str
    label: float