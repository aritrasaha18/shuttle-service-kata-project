FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

# install dependencies
RUN pip3 install requests

RUN pip3 install flask

COPY . .

EXPOSE 8081

CMD [ "python3", "requestShuttle.py" ]
