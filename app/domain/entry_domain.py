from pydantic import BaseModel

class EntryDomain(BaseModel):
    input: str
    output: str
    label: float