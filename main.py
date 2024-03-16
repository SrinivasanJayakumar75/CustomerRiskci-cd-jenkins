
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import pandas as pd 
from fastapi.middleware.cors import CORSMiddleware
from prediction_model.predict import generate_predictions 

app = FastAPI(
    title="CustomerRiskAnalysis App using API - CI CD Jenkins",
    description = "A Simple CI CD Demo",
    version='1.0'
)

origins=[
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class CustomerRisk(BaseModel):
    id: float
    fea_1: float
    fea_2: float
    fea_3: float
    fea_4: float
    fea_5: float
    fea_6: float
    fea_7: float
    fea_8: float
    fea_9: float
    fea_10: float
    fea_11: float


@app.get("/")
def index():
    return {"message":"Welcome to CustomerRiskAnalysis App using API - CI CD Jenkins" }

@app.post("/prediction_api")
def predict(customer_details: CustomerRisk):
    data = customer_details.model_dump()
    prediction = generate_predictions([data])["prediction"][0]
    if prediction == "1":
        pred = "Customer is in Risk"
    else:
        pred = "NO Risk"
    return {"status":pred}

@app.post("/prediction_ui")
def predict_gui(
       id: float,
    fea_1: float,
    fea_2: float,
    fea_3: float,
    fea_4: float,
    fea_5: float,
    fea_6: float,
    fea_7: float,
    fea_8: float,
    fea_9: float,
    fea_10: float,
    fea_11: float):

    input_data = ['id', 'fea_1', 'fea_2', 'fea_3', 'fea_4', 'fea_5', 'fea_6', 'fea_7', 'fea_8', 'fea_9', 'fea_10', 'fea_11']
    
    cols = ['id', 'fea_1', 'fea_2', 'fea_3', 'fea_4', 'fea_5', 'fea_6', 'fea_7', 'fea_8', 'fea_9', 'fea_10', 'fea_11']
    
    data_dict = dict(zip(cols,input_data))
    prediction = generate_predictions([data_dict])["prediction"][0]
    if prediction == "1":
        pred = "Customer is in Risk"
    else:
        pred = "NO Risk"
    return {"status":pred}

if __name__== "__main__":
    uvicorn.run(app, host="0.0.0.0",port=8005)
