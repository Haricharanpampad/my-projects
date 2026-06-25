# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:40:21 2026

@author: haria
"""

import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('C:/Users/haria/OneDrive/Pictures/Desktop/ML projects/trained_model.sav', 'rb'))

def Diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    
    
    #title 
    st.title('Diabetes Prediction Web App')
    
    #input data
    Pregnancies=st.text_input('Number of pregnencies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('BloodPressure')
    SkinThickness=st.text_input('SkinThickness')
    Insulin=st.text_input('Insulin')
    BMI=st.text_input('BMI')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
    Age=st.text_input('Age')
    
    #code for prediction
    diagnosis=''
    
    #creating button
    if st.button('Diabetes Test Result'):
        diagnosis=Diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)





if __name__ == '__main__':
    main()
    
  
        
      
