from sqlalchemy.orm import Session
from model import SearchHistory
from typing import List

class SearchHistoryRepo:
    def __init__(self, db: Session):
        self.db = db
    
    def create_history(self, user_id: int, query: str, response: str) -> SearchHistory:
        """Create a new search history entry."""
        history = SearchHistory(
            user_id=user_id,
            query=query,
            response=response
        )
        self.db.add(history)
        self.db.commit()
        self.db.refresh(history)
        return history
    
    def get_user_history(self, user_id: int) -> List[SearchHistory]:
        """Get all search history for a specific user."""
        return self.db.query(SearchHistory).filter(
            SearchHistory.user_id == user_id
        ).order_by(SearchHistory.timestamp.asc()).all()
