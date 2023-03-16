# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:19:21 2023

@author: jrelh
"""

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved machine learning model
model = joblib.load('regression_model_saved.joblib')

# Define the API endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()
    
    # Extract the features from the JSON data
    category = data['Category']
    accident_type = data['Accident_type']
    year = data['year']
    month = data['month']
    
    category = 'Category_' + category
    accident_type = 'Accident_Type_' + accident_type
    month = 'Month_' + month
    
    dummies_columns = ['Year', 'Category_Alkoholunfälle', 'Category_Fluchtunfälle',
       'Category_Verkehrsunfälle', 'Accident_Type_Verletzte und Getötete',
       'Accident_Type_insgesamt', 'Accident_Type_mit Personenschäden',
       'Month_01', 'Month_02', 'Month_03', 'Month_04', 'Month_05', 'Month_06',
       'Month_07', 'Month_08', 'Month_09', 'Month_10', 'Month_11', 'Month_12']
    
    vector_input = []
    vector_input.append(year)
    vector_input.append(category)
    vector_input.append(accident_type)
    vector_input.append(month)
    
    value_input = []
    for col in dummies_columns:
        if col in vector_input:
            value_input.append(1)
        else:
            value_input.append(0)
        
    value_input[0]=vector_input[0]
    
    
    df = pd.DataFrame(columns=dummies_columns)
    df.loc[len(df)] = value_input
    
    
    # Use the loaded model to make a prediction
    prediction = model.predict(df)
    prediction = prediction.astype(int)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0]})



if __name__ == '__main__':
    app.run()
