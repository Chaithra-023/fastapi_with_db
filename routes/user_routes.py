from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from repositories.user_repo import userRepo
from schemas.User_schema import UserSchema
router = APIRouter()

@router.post("/signup")
def signup(db: Session = Depends(get_db)):
    user_repo = userRepo(db)
    user_repo.add_user(user)
    return {"message": "User created successfully"}

@router.post("/login")
def login():
    return {"message": "User logged in successfully"}

