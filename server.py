from fastapi import FastAPI
from pydantic import BaseModel
from src.calculate import add_plus, add_multiply

app = FastAPI() 

class RequestAddPlus(BaseModel): 
    num1: float
    num2: float

@app.post("/add-plus")
def add_plus_endpoint(req: RequestAddPlus): 
    return {"result": add_plus(req.num1, req.num2)}



@app.post("/add-multiply")
def add_multiply_endpoint(req: RequestAddPlus): 
    return {"result": add_multiply(req.num1, req.num2)}