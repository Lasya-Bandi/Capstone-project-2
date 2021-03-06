# set the base image 
FROM python:3.6
# File Author / Maintainer
MAINTAINER Lasya Bandi
#add project files to the usr/src/app folder
ADD . /home/lasya/demo
#set directoty where CMD will execute 
WORKDIR /home/lasya/demo
COPY requirements.txt ./
# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt
# Expose ports
EXPOSE 8000
# default command to execute    
CMD exec gunicorn demo.wsgi:application --bind 0.0.0.0:8000 --workers 3 

FROM jenkins:1.596
 

 

