import uuid
from fastapi import FastAPI, HTTPException, status, Response

from app.model import Author, AuthorView
from app.db import authors

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "hello world"}

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/api/v1/authors")
async def all_authors():
    return {"data" : list(authors.values())}

@app.get("/api/v1/authors/{id}")
async def author_by_id(id: str):
    if id not in authors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"author with id: {id} was not found"
        )

    return {"data" : authors[id]}

@app.post("/api/v1/authors", status_code=status.HTTP_201_CREATED)
async def create_posts(author: AuthorView):
    new_author = Author(
        authorid=str(uuid.uuid4()), 
        firstname=author.firstname, 
        lastname=author.lastname, 
        birthyear=author.birthyear,
        books=author.books)

    authors[new_author.authorid] = new_author

    return {"data": new_author}

@app.delete("/api/v1/authors/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(id: str):
    if id not in authors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"author with id: {id} was not found"
        )
    
    authors.pop(id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/v1/authors/{id}")
async def update_author(id: str, author: AuthorView):
    if id not in authors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"author with id: {id} was not found"
        )

    updated_author = Author(
        authorid=str(uuid.uuid4()), 
        firstname=author.firstname, 
        lastname=author.lastname, 
        birthyear=author.birthyear,
        books=author.books)
    
    authors[id] = update_author

    return {"data": updated_author}

@app.get("/api/v1/authors/{id}/books")
async def author_books(id: str):
    if id not in authors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found"
        )

    author = authors[id]

    return {"books" : author.books}