from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model once at startup
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Extract features in the same order as training
    features = [
        data['Store_id'],
        data['Store_Type'],
        data['Location_Type'],
        data['Region_Code'],
        data['Holiday'],
        data['Discount'],
        data['Order'],
        data['Month'],
        data['DayOfWeek'],
        data['WeekOfYear'],
        data['IsWeekend']
    ]
    
    prediction = model.predict([features])[0]
    
    return jsonify({
        'predicted_sales': round(float(prediction), 2),
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
