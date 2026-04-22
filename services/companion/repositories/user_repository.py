'''
Este archivo conecta a la base de datos,
lee modelos para basarse como un mapa,
aqui se va a inyectar solo la dependencia
para la conexion a la DB.
'''

'''
from sqlmodel import Session
from backend.services.companion.models.user_models import User
#from backend.services.companion.databases.db import engine  ###Import para ejemplo de uso, no es necesario para la clase en sí.


class UserRepository:

    def create_user(self, session: Session, user: User) -> User:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
'''


''' 🔽 EJEMPLO DE USO CODIGO PARA CREAR USSUARIO DE EJEMPLO
if __name__ == "__main__":
    repo = UserRepository()

    with Session(engine) as session:
        new_user = User(username="marcial", password="1234")

        created_user = repo.create_user(session, new_user)

        print("Usuario creado:", created_user)'''