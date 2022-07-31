from pydantic import BaseModel
from typing import Optional, List

class Book(BaseModel):
    title: str
    published: int

class Author(BaseModel):
    authorid: str
    firstname: str
    lastname: str
    birthyear: int
    books: Optional[List[Book]]

class AuthorView(BaseModel):
    firstname: str
    lastname: str
    birthyear: int
    books: Optional[List[Book]]


