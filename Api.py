from fastapi import FastAPI
from src.DataSchema.schema import Patient
from src.pipeline.prediction_pipeline import Prediction
from src.logger import logging
import sys
from src.exception import CustomException
app=FastAPI()
@app.get('/')
def welcome():
    return {'message':'Welocome to heart health prediction model api.'}

@app.post('/predict')
def predict(patient:Patient):
    input_data={
        'Age':patient.Age,
        'Gender':patient.Gender,
        'Heart_rate':patient.Heart_rate,
        'Systolic_blood_pressure':patient.Systolic_blood_pressure,
        'Diastolic_blood_pressure':patient.Diastolic_blood_pressure,
        'Blood_sugar':patient.Blood_sugar
    }
    try:
        pred_obj=Prediction(input_data)
        pred=pred_obj.predict()
        logging.info("prediction done successfully in api")
        return {"prediction":int(pred[0])}
    except Exception as e:
        raise CustomException(e,sys)
