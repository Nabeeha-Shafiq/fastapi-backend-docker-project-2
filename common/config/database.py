from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from common.config.settings import settings  # <--- IMPORTANT: Updated import path
from common.config.logger import logger # We'll add logger here when it's in common/config too

# The DATABASE_URL is read from our centralized settings
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for our declarative models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        logger.debug("Database session opened") 
        yield db
    finally:
        db.close()
        logger.debug("Database session closed") 

#automatically maps classes made in models/user.py to db tables 
def create_db_tables(): 
    """Automatically creates db tables for the model classes defined in /models inheriting from Base defined above"""
    from user_service.models import user
    Base.metadata.create_all(bind=engine)
    logger.info("DB tables created successfully")