# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE core.settings

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Copy the requirements file into the container and install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the Django project into the container
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

