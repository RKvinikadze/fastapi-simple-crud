# REST with FastAPI

simple REST api using fastapi.

# Preconditions

Install [Python3](https://www.python.org/downloads/)

Check python version with `python --version`

## To run project 

You need to install project requirements with command:

`pip install -r requirements.txt`

And then, run project on port 8000 with:

`uvicorn app.main:app --reload --port 8000`

## Run with Docker
---
### Pull image
```
docker pull rkvinikadze/simple-rest-fastapi
```
---
### Run container on port 8000 
```
docker run -ti -p 8000:8000 rkvinikadze/simple-rest-fastapi
```
`After this command, you can check result on localhost:8000`

### Automatic docs
You can check interactive API documentation on `application_url/docs` (**Swagger**) or `application_url/redoc` (**Redoc**)

