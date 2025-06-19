from setuptools import setup, find_packages

setup(
    name="user_service", 
    version="1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.111.0",                 
        "uvicorn[standard]==0.30.1",        
        "psycopg2-binary==2.9.9",           
        "SQLAlchemy==2.0.30",               
        "python-dotenv==1.0.1",             
        "pydantic-settings==2.3.4",         
        "passlib[bcrypt]==1.7.4",           
        "bcrypt==4.1.2",
        "python-jose[cryptography]==3.3.0",
    ],
    include_package_data=True,
    zip_safe=False,
)
