from setuptools import setup, find_packages

setup(
    name="user_service", 
    version="1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.111.0",                 # Web framework
        "uvicorn[standard]==0.30.1",        # ASGI server with Swagger support
        "psycopg2-binary==2.9.9",           # PostgreSQL driver
        "SQLAlchemy==2.0.30",               # ORM
        "python-dotenv==1.0.1",             # Load environment variables
        "pydantic-settings==2.3.4",         # Strong schema management
        "passlib[bcrypt]==1.7.4",           # Password hashing
    ],
    include_package_data=True,
    zip_safe=False,
)
