from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="POO1")):
    data = load_file()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"), order: str = Query("asc", description="Sort order: asc or desc")):
    
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by field. Must be one of {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'")
    
    data = load_file()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data
