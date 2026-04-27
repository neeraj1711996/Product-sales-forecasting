from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model once when server starts
model = joblib.load('model.pkl')

# Route 1: Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route 2: Prediction API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    features = [[
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
    ]]
    
    prediction = model.predict(features)[0]
    
    return jsonify({
        'predicted_sales': round(float(prediction), 2),
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
