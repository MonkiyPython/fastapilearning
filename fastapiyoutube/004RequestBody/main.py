from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn  # noqa;

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


# While Creating a Class we need to consider the Parameters with Type
class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


# If I need to send Request Body Always need to create with parameters
# So We're extending Base Class from Pydantic
@app.post("/blog/")
def create_blog(blog: Blog):
    return {"data": f"Blog is Created with title as {blog.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
