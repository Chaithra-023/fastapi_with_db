from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SearchHistoryBase(BaseModel):
    query: str
    response: str

class SearchHistoryCreate(SearchHistoryBase):
    pass

class SearchHistory(SearchHistoryBase):
    id: int
    user_id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True
