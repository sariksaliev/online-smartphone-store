# security.py
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'Sardorbek-uaef98bg9824b9834g98'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE = 30


# Наша JWT тут создает токен
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({'expires': expire.isoformat()})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
