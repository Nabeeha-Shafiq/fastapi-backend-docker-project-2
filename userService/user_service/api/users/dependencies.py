from fastapi import Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session #gotta know db session 
#this dependences,.py file ascta like the security guard for our app , it verifires anyone enterimg via access tokens 
#access tokens ==badge 

from common.config.database import get_db 
from common.config.logger import logger
from user_service.models import user as user_model 
from fastapi.security import OAuth2PasswordBearer
#from user_service.auth import verify_token 
#changes path for common use 
from common.config.auth import verify_token
#yahan we specify what endpoints we gotta inject via Dependencoes and like urls 
#cool feature of oauth2PasswordBEarer it injects deendencies directly into all our api endpoints 
#this tells fastapi hey if u need entrance the door is /login api go there dude
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")
#this is the actual security guard function
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)): #depends on current db session
    logger.debug("Current user verifying themselves via access token aka badge")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, #client side exception throw and tell em sorry ur not allowed into the fight club
        detail="Could not validate credentials, user kicked out of our club",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = verify_token(token)
    if payload is None:
        logger.warning("Token verification failed, raising credentials exception.User kicked out of our club")
        raise credentials_exception
    username: str = payload.get("sub")
    if username is None:
        logger.warning("Token payload missing 'sub' (username), raising credentials exception.")
        raise credentials_exception
    user = user_model.User = db.query(user_model.User).filter(user_model.User.userName == username).first()
    if user is None:
        logger.warning(f"User '{username}' not found in DB from token, raising credentials exception.")
        raise credentials_exception
    logger.info(f"User '{user.userName}' successfully authenticated.Welcome to the club man ! lezz go")
    #obv return user resuls
    return user
