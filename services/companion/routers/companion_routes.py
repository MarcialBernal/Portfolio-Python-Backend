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
from companion.schemas.chat_schemas import ChatResponse, ChatRequest 
from backend.services.companion.dependencies.companion_dependency import call_companion_service
from backend.services.companion.dependencies.auth_dependency import get_current_user
from backend.services.companion.schemas.user_schemas import User

router = APIRouter()

# Endpoint para el servicio de companion, protegido por autenticación
@router.post("/chat", response_model = ChatResponse)
async def companion(request: ChatRequest, call_companion = Depends(call_companion_service), user = Depends(get_current_client)):
    return call_companion(request.messages)


# Endpoint de login para obtener el token de autenticación
@router.post("/login")
def login(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user