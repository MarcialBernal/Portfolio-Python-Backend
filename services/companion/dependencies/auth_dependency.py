from fastapi import Depends
from typing import Annotated
from backend.services.companion.auth.security import oauth2_scheme

#crea una dependencia que se encargará de verificar el token y devolver la información del usuario
#La funcion de fake_decode_token es una función de ejemplo que simula la decodificación de un token y devuelve un objeto User con información ficticia. 
# En una implementación real, esta función debería verificar el token y extraer la información del usuario de manera segura.
from backend.services.companion.schemas.user_schemas import User

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user