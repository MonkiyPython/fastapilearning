[![wakatime](https://wakatime.com/badge/github/MonkiyPython/fastapilearning.svg)](https://wakatime.com/badge/github/MonkiyPython/fastapilearning)



Features of FastAPI

- Automatic Docs
  - Swagger UI
  - ReDoc
- Uses Modern Python Features
  - Provides support for typing [Type Hints]
- Based on Open Standards [Standard way of writing API according to Linux Foundation]
  - JSON Schema
  - Open API
- Code Editors Autocomplete like VSCode and PyCharm
  - It'll be achieved using pydantic
- Security and Authentication
  - HTTP Basic
  - OAuth2 [Also known as JWT Tokens]
  - API Keys in
    - Headers
    - Query Paramenters
    - Cookies, etc.
- Dependency Injection
  - Unlimited Plugins 
  - Testing
- Starlette Features [Since FastAPI builts on Starlette]
  - Provides WebSocket Support 
  - GraphQL Support
  - In-Process background Tasks.
  - Startup and Shutdown Events.
  - Test client built on requests.
  - CORS, GZip, Static Files, Streaming Responses.
  - Session and Cookie Support.
- Other Supports
  - SQL Databases
  - NOSQL Databases
  - GraphQL Support



**Sebastian Ramirez** is the Author of FastAPI

Requirements

- Python 3.6 +
- Need to have FastAPI and Uvicorn Libraries,
- ```pip install fastapi```
- ```pip install uvicorn```



### Running a Simple FastAPI Server consisting of 2 routes

-  index
- about

```python
from fastapi import FastAPI  # Importing Library

app = FastAPI()  # Creating a instance


@app.get("/")  # Routing to index page
# Routing to index page [In FastAPI here '/' call as Path, 'get' is called as Operation, '@app' is path operation Decorator]
def index():  # Creating a index Function
    return {"data": {"name": "Rajath"}}  # Response in JSON


@app.get("/about")
def about():  # Creating a about Function
    return {"data": "about page"}
```

```bash
uvicorn main:app --reload
```

### PATH Parameters

```python
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
```

```bash
uvicorn main:app --reload
```

### Query parameters (Limit, Optional an Others)

```python
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

```

### Request Body / Body Parameters

```python
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

```

