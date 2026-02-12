from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from utils.ai_response import get_completion
from schemas.ai_response_schemas import AIRequest, AIResponse
from dependencies import get_current_user
from model import User
from repositories.history_repo import SearchHistoryRepo

router = APIRouter()


@router.post("/ask", response_model=AIResponse)
def ask_ai(
    request: AIRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get response from AI model and save to history."""
    try:
        response = get_completion(request.message, request.system_prompt)
        
        # Save to history
        history_repo = SearchHistoryRepo(db)
        history_repo.create_history(
            user_id=current_user.id,
            query=request.message,
            response=response
        )
        
        return AIResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
