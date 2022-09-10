#Pull Base Image
FROM python:3.10.4-slim-bullseye

#Set Environment Variables
ENV PIP_DISABLE_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory

WORKDIR /code

#Install Dependancies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copy project
COPY . .