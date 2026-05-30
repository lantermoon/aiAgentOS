from fastapi import APIRouter, Depends

from app.controllers.base import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse

router = APIRouter(prefix="/api/v1/home", tags=["home"])


@router.get("", response_model=UserResponse)
def home(current_user: User = Depends(get_current_user)):
    return current_user