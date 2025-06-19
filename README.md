Docker Containerized CRUD Application

Project Description 
This project aims to give hands on practise on coding via FastAPI , maintaining standard file structure , godd code practices like fucntion descripors and pep8 , the app is also containerized via Docler compose with 3 services 
1- FastAPI Web Service 
2- PostgreSQL DB Service
3- MongoDB Service

Tech Stack Used
Backend Code : FastAPI (Python Language)
Containerization : Docker Compose
Database (User Management) : PostgreSQL

fastapi-backend-project/
│
├── common/                  # Shared project-wide configurations
│   └── config/
│       ├── database.py      # <--- DATABASE CONNECTION (SHARED)
│       └── settings.py      # <--- APP SETTINGS (SHARED)
│
├── user-service/            # Your user microservice
│   └── user_service/        # Python package for user service
│       ├── app.py           # Main FastAPI app for user service
│       ├── api/users/
│       ├── crud/
│       ├── models/
│       └── schemas/
│
├── .env
├── docker-compose.yml
└── README.md
