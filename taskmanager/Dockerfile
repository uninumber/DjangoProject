# base image  
FROM python:3.10.5   
# setup environment variable  
ENV DockerHome=ligraus314/Desktop/HH.ru/taskmanager  

# set work directory  
RUN mkdir -p $DockerHome 

# where your code lives  
WORKDIR $DockerHome  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHome  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver 