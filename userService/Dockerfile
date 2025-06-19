# #a pyhton base image cz like core is python
# # this is like the bread and butter need for the app 
# #like python is the ultimate basic need here 
# #, and the slim-buster is like a tag==version its not just a fancy name 
# #it is a version known for being lightweight and functional avoiding documentation 
# FROM python:3.10-slim-buster
# #this is the directory from where all app will be run in the container
# #this was not set to project root cz
# WORKDIR /app 
# #everything in container is gonna be done relative to this app 

# #now since /app directory sey kaam ho raha hey main os gotaa copy the requiremtnts txt there
# #COPY ./setup.py ./ 
# COPY ./userService/setup.py ./

# #find the setup.py from host folder and copy it to my  current working directory which is /app
# #COPY ./user_service  ./user_service
# COPY ./userService/user_service ./user_service
# COPY ./common ./common

# #find the /user_service from host and copy it to my root directory ie app/user_services
# #now container looks like
# #/app/
# #├── setup.py
# #└── user_service/
# #   └── app.py, routes, and all

# #this would install all dependencies in requiremrnts.txt
# #why the r 
# RUN pip install --no-cache-dir -e .
# #run the setup.py in the root directory ie app


# # now this is a multiple services app meaning it has 
# #postresql db sercive 1---> container 1
# #mongodb service 2 ---> container 2
# #fastapi servise 3 ----> container 3
# # so we need docker compose to bing all these services on a singular network
# #the port on which application will bind


# EXPOSE 8000 
# #only for docuentation puposes just to clear out things about port mapping

# #the netwoek 0.0.0.0 has this feature that it can not only listen to local and private connections 
# #but it can bind with any available connections , other containers and all 
# # main command that will be used to run all app , like the one command i use locally 
# CMD ["uvicorn","user_service.app:app","--host","0.0.0.0","--port","8000"]
# #user_service.app----> means: /app/user_service/app.py

# userService/Dockerfile
FROM python:3.10-slim-buster

WORKDIR /app # All operations in the container will be relative to /app

# Copy setup.py for the userService package
COPY ./userService/setup.py ./

# Copy the userService Python source code
COPY ./userService/user_service ./user_service

# Copy the common package
# Since build context is '.', ./common refers to fastapi-backend-project/common
COPY ./common ./common

# Install the userService package in editable mode
# This uses the setup.py copied to /app/setup.py
RUN pip install --no-cache-dir -e .

# Now, explicitly install the 'common' package from its copied location within /app
# No need to change WORKDIR here, as the path is absolute from /app
RUN pip install --no-cache-dir -e ./common

EXPOSE 8000

# CMD is correct for the userService Python package
CMD ["uvicorn", "user_service.app:app", "--host", "0.0.0.0", "--port", "8000"]