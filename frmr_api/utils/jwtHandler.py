import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette import status
from frmr_api.utils.config import SECRET_KEY


def authorize_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    try:
        decodedToken = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if decodedToken['admin']:
            return
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            headers={"WWW-Authenticate": "Bearer"}
        )

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def create_jwt_token() -> str:
    expiration = datetime.utcnow() + timedelta(days=9999)
    payload = {
        "exp": expiration,
        "sub": "permissions",
        "methods": ["POST", "GET"],
        "admin": True
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
