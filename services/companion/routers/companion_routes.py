'''
Aqui solo se inyecta la dependencia 
de services(CRUD O SEA LOGICA), 
y autenticacion, en este caso concreto,
tambien aqui se integran los schemas.
Request, Response (si necesitas)
Headers, cookies (si aplica)
'''
    
from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session
from services.companion.schemas.user_schemas import UserResponse
from services.companion.database.session import get_session
from services.companion.use_cases import user_services as user_service

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
def get_users(session: Annotated[Session, Depends(get_session)]):
    return user_service.get_users(session)