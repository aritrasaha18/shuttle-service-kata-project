# base image
FROM python:3.8-slim-buster

# set working directory
WORKDIR /app

# copy the requirements file to the container
COPY requirements.txt .

# install dependencies
RUN pip3 install pymongo

RUN pip3 install flask

# copy the application code to the container
COPY . .

# expose the port for the web application
EXPOSE 8085

# start the web application
CMD ["python3", "database.py"]
