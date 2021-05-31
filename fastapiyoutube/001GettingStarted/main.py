from fastapi import FastAPI  # Importing Library

app = FastAPI()  # Creating a instance


@app.get(
    "/"
)  # Routing to index page [In FastAPI here '/' call as Path, 'get' is called as Operation, '@app' is path operation Decorator]
def index():  # Creating a index Function
    return {"data": {"name": "Rajath"}}  # Response in JSON


@app.get("/about")
def about():  # Creating a about Function
    return {"data": "about page"}
