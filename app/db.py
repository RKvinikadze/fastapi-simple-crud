import uuid
from app.model import Author, AuthorView, Book

author1 = Author(authorid=str(uuid.uuid4()), firstname="William", lastname="Faulkner", birthyear=1897)

author2 = Author(authorid=str(uuid.uuid4()), firstname="George", lastname="Martin", birthyear=1948, books=[Book(title="A Game Of Thrones", published=1996)])

authors = {
    author1.authorid:author1,
    author2.authorid:author2
}


