from sqlalchemy.orm import Session # db session that will get passed to every function ka as first parameter
from user_service.models import user as user_model #alias user_model for like clarity 
from user_service.schemas import user as user_schema #alias schema
from common.config.logger import logger
import bcrypt
#CRUDS

#create
# def create_user(db: Session , userobj: user_schema.UserCreate):
#     logger.debug(f"A new user just attemplted to log in to the system , username ",{userobj.username})
#     #db_user=user_model.User(username,password)
#     hashed_password = bcrypt.hashpw(userobj.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#     db_user = user_model.User(userName=userobj.userName, password=hashed_password) 
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user) #extends the userDB with attributes like id and created by 
#     logger.info(f"New user ",{userobj.username},"successfully logged in to the system")
#     return db_user

# def get_user_by_username(db:Session,username : str) :
#     userRetrieved=db.query(user_model.User).filter(user_model.User.userName==username).first() #select from WHERE username=given username query on sql backend 
#     return userRetrieved
def create_user(db: Session, user: user_schema.UserCreate): # <--- Changed parameter name here
    logger.debug(f"A new user just attempted to register to the system, username: {user.userName}") # Corrected log message

    # Use the 'user' parameter consistently here
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    db_user = user_model.User(userName=user.userName, password=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    logger.info(f"New user '{user.userName}' successfully registered to the system.") # Corrected log message
    return db_user

def get_user_by_username(db: Session, username: str):
    userRetrieved = db.query(user_model.User).filter(user_model.User.userName == username).first()
    return userRetrieved
