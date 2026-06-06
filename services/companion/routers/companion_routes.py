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
from services.companion.dependencies.service_dependency import get_user_service

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
def get_users(session: Session = Depends(get_session), service = Depends(get_user_service)):
    return service.get_all_users(session)

'''
@router.get("/users", response_model=list[UserResponse])
def get_users(
    session: Session = Depends(get_session)
):
    repository = UserRepository(session)
    service = UserService(repository)

    return service.get_all_users()
    
En este caso, se inyectan todas las dependencias en la ruta. 
'''
