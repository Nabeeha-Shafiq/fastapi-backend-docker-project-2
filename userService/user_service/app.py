from fastapi import FastAPI
from common.config.logger import logger
#instead of using print statements using a logger , reason idk cz they do it this way dont know why 
from common.config.settings import settings
from common.config.database import create_db_tables
app = FastAPI(
    title="User Media App coded via FastAPI and Docker containerized and all",
    description="Features include user management + i,ahe upload capability , a bit of AI",
    version="1",
    docs_url="/docs",
    redoc_url="/redoc",
)
@app.on_event("startup")
async def startup_event():
    """
    Event handler that runs when the FastAPI application starts up.
    Used to create database tables
    """
    logger.info("App startup : initializing DB tables")
    create_db_tables()
    logger.info("App startup complete , tables are made in DB")

@app.get("/")
async def root():
    """
    Root endpoint for the API.
    Returns a welcome message.
    """
    logger.info("Root endpoint called")
    return {"message": "User Media App coded via FastAPI and Docker containerized and all"}

@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Used to verify if the API is running.
    """
    logger.info("Health check endpoint called.")
    return {"status": "ok", "message": "API is happy and healthy"}

# will add more crud parts to it later on 