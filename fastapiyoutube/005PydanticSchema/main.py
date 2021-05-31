from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"Blog list of {limit} from db"}
    else:
        return {"data": "Blog list of 10"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "All Unpublished Blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10):
    return {"data": {"1", "2"}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post("/blog/")
def create_blog(blog: Blog):
    return {"data": f"Blog is Created with title as {blog.title}"}
