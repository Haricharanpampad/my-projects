# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 00:58:02 2026

@author: haria
"""

from pydantic import BaseModel #sets formates of input data
import pickle #for loading saved model
import json


app=FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int
    
    
    
diabetes_model=pickle.load(open('diabetes_model.sav','rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters :model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    
    preg=input_dictionary['Pregnancies']
    glu=input_dictionary['Glucose']
    bp=input_dictionary['BloodPressure']
    Skin=input_dictionary['SkinThickness']
    insulin=input_dictionary['Insulin']
    bmi=input_dictionary['BMI']
    bpf=input_dictionary['DiabetesPedigreeFunction']
    age=input_dictionary['Age']
    
    
    input_list=[preg,glu,bp,Skin,insulin,bmi,bpf,age]
    prediction=diabetes_model.predict([input_list])
    if prediction[0]==0:
        return 'the person is not Diabetic'
    else:
        return 'the person is  Diabetic'
    
    
    