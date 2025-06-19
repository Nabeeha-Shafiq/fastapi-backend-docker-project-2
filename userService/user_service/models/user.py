from sqlalchemy import Column,Integer,String,Boolean,DateTime
from sqlalchemy.sql import func
from common.config.database import Base
#it shall inherit the base defined in sql bas karna hey to karna hey eof
class User(Base):
    """SQLAlchemy scehma relating to user table is sql and user class in python"""
    __tablename__="users" #plural rememeba sql rules
    id=Column(Integer,primary_key=True,index=True)
    userName=Column(String,unique=True,index=True,nullable=False)
    password=Column(String,nullable=False) # unique contraint not added cz we;d do hashing/encryption of password wesey bhi so that'll be fixed 
    created_at=Column(DateTime(timezone=True),server_default=func.now()) #funcnow gets the current system time
#for when i print user object
def __repr__(self):
        return f"<User(id={self.id}, userName='{self.userName}')>"
