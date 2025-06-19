from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from common.config.database import get_db
from common.config.logger import logger
#from user_service.auth import create_access_token
from common.config.auth import create_access_token
from user_service.crud import user as crud_user
from user_service.schemas import user as user_schema
from user_service.api.users.dependencies import get_current_user # Our bouncer!
import bcrypt
from user_service.models import user as user_model
#router auto adds the prefix url behind evey endpoint 
#tags is just for pretty UI groupd all user related ops under users heading
router=APIRouter(prefix="/api/v1/users",tags=["Users"])
@router.post("/login",response_model=user_schema.Token)
#see this form_data is a v cool thing that automatically formats reuwsts and resposes for u 
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    logger.info(f"Login request for USer with username: {form_data.username}")
    user = crud_user.get_user_by_username(db, username=form_data.username)
    if not user: #if username wrong
        logger.warning(f"Login failed !!! for User with username '{form_data.username}' not found.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, #send a client side error
            detail="Incorrect username ",
            headers={"WWW-Authenticate": "Bearer"},#dont know what this does 
        )
    # if password incorrect
    if not bcrypt.checkpw(form_data.password.encode('utf-8'), user.password.encode('utf-8')):
        logger.warning(f"Login failed: Incorrect password for user '{form_data.username}'.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
#if password correct then go on to verity for access tokens
    access_token = create_access_token(data={"sub": user.userName})
    logger.info(f"User '{user.userName}' logged in successfully.")
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/", response_model=user_schema.UserResponse, status_code=status.HTTP_201_CREATED)
async def create_new_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Attempting to create user: {user.userName}")
    db_user = crud_user.get_user_by_username(db, username=user.userName)
    if db_user:
        logger.warning(f"User creation failed: Username '{user.userName}' already registered.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    new_user = crud_user.create_user(db=db, user=user)
    logger.info(f"User '{new_user.userName}' created successfully.")
    return new_user

# A protected route example using our bouncer
@router.get("/me", response_model=user_schema.UserResponse)
async def read_current_user(current_user: user_model.User = Depends(get_current_user)):
    logger.info(f"Accessed /me for user: {current_user.userName}")
    return current_user