# Parth Desai - Website

This is my own website, where I sell services and show projects which I've done before.


## Project Setup

Python Version: 3.9


### Set Python Virtual Environment (recommended)

Install [Python Virtual Environment](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)

To Activate virtual environment

For Linux

    source myenv/bin/activate 

For Windows

    myenv\Scripts\activate


### Install Required Python Packages

    pip install -r requirements.txt


### Create Environment

Create `.env` file

    # For Linux
    cp sample_env.txt .env

    # For Windows
    copy sample_env.txt .env


Change environment variables in `.env` file

#### Variables Description

- `DB_NAME`: `database_name`
- `DB_USER`: `database_user_name`
- `DB_PASS`: `database_user_password`
- `DB_PORT`: `database_port`
- `DB_HOST`: `database_host`


### Database Migrations

Run below commands to create tables in database

    python manage.py makemigrations
    python manage.py migrate


### Run Server

To run Local Development Server, run below cmd

    python manage.py runserver

To run using GUNICORN

    gunicorn core.wsgi:application --bind 0.0.0.0:8000 --timeout 600 --daemon

To save db data into json files

    python manage.py dumpdata dashboard.Skill dashboard.Contact > dashboard.json
    
    python manage.py dumpdata blog.Category blog.Post blog.Comment > blog.json
    
    python manage.py dumpdata accounts.User > accounts.json
    
    python manage.py dumpdata project.Project > project.json
