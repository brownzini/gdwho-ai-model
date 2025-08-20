from pydantic import BaseModel
from typing import List

from app.domain.entry_domain import EntryDomain

class TrainingRequest(BaseModel):
    id: int
    entries: List[EntryDomain]