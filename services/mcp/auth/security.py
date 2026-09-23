from fastapi.security import OAuth2PasswordBearer


#instancia la clase OAuth2PasswordBearer con la URL del endpoint de login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


