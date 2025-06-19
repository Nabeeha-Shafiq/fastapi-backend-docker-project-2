# from pydantic_settings import BaseSettings, SettingsConfigDict
# import os

# class Settings(BaseSettings):
#     #tells the app where to look for environment variable settings and all
#     #extra ignore k liye it wont complain or smth if in .env we have more variables than in basesettings
#     model_config=SettingsConfigDict(env_file=".env",extra="ignore")
#     #db url comes from .env 
#     DATABASE_URL: str

#     PROJECT_NAME="User Media Services Fastapi Dockerized app"
#     #secret key as in .env file
#     SECRET_KEY: str="i_am_top_secret_but_i_need_to_be_superlong_for_Security_reasons"
#     #its good practise to put version wth api url for like scalability , clarity etc
#     API_V1_STR: str="api/v1"
# #object gotta make  
# settings=Settings()

# common/config/settings.py (After fix)
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar # Import ClassVar for constants not meant to be settings fields

class Settings(BaseSettings):
    # Project-related constants (can be ClassVar if not loaded from env)
    PROJECT_NAME: ClassVar[str] = "User Media Services Fastapi Dockerized app"
    API_V1_STR: ClassVar[str] = "/api/v1" # Or simply str if it can come from env

    # Database connection settings (these should be loaded from .env)
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()