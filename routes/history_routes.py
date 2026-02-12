from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from dependencies import get_current_user
from model import User
from repositories.history_repo import SearchHistoryRepo
from schemas.history_schemas import SearchHistory
from typing import List

router = APIRouter()

@router.get("/history", response_model=List[SearchHistory])
def get_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get search history for the authenticated user."""
    history_repo = SearchHistoryRepo(db)
    return history_repo.get_user_history(current_user.id)
