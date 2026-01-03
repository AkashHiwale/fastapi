from fastapi import FastAPI
import json

def load_file():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "This API manages patient records and provides information about patients."}

@app.get("/view")
def view_data():
    data = load_file()
    return data