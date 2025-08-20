from pydantic import BaseModel
from typing import List

from app.domain.entry_domain import EntryBase

class TrainingRequest(BaseModel):
    id: int
    entries: List[EntryBase]