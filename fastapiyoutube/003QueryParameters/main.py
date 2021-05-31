from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# It's Super ineffecient to retrieve all the blogs.
@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # Only get 10 published blogs by handling query parameters [/blog?limit=10&published=true]
    # We can Use QueryParmater: QueryParameter[Type] = DefaultValue
    # If Something Optional we can use QueryParameter: Optional_KeyWord_Imported_from_Typing[Type] = DefaultValue
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
    # return {"no of comments": limit}
    return {"data": {"1", "2"}}
