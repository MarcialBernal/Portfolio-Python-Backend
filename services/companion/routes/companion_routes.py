'''
Aqui solo se inyecta la dependencia 
de services(CRUD O SEA LOGICA), 
y autenticacion, en este caso concreto,
tambien aqui se integran los schemas.
Request, Response (si necesitas)
Headers, cookies (si aplica)
'''
    
from fastapi import APIRouter, Depends
from companion.schemas.chat_schemas import ChatResponse, ChatRequest 
from dependencies.service_dependencies import call_companion_service

router = APIRouter()

@router.post("/companion", response_model = ChatResponse)
async def companion(request: ChatRequest, call_companion = Depends(call_companion_service)):
    return call_companion




