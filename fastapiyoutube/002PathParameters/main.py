from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": "Blog List"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "All Unpublished Blogs"}


@app.get("/blog/{id}")  # Dynamic Data should be inside the '{ }' Paranthesis
def show(
    id: int,
):  # Dynamic Data should be accepted by the Function, int is 'Type' for the paramenters
    # fetch blog id = id
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int):
    # fetch comments of blog id = id
    return {"data": {"1", "2"}}


# Hierachy
"""
1. /
2. /blog/unpublished
3. /blog/id/
4. /blog/id/comments
"""
