from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import numpy as np
from flask_cors import CORS 
import os
print(os.path.exists('calorie_model.pkl'))

app = Flask(__name__)

CORS(app)

# Load the trained model
try:
    model = joblib.load('calorie_model.pkl')
    print("Model loaded successfully!")
    print(model)

except Exception as e:
    print(f"Error loading model: {e}")
# print(os.listdir('.'))


# # features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
# prediction = model.predict(features)
# print(prediction)
@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     print("Request method:", request.method)
#     if model is None:
#         return jsonify({"error": "Model not loaded!"}), 500
    
#     try:
#         data = request.form.to_dict()
#         print("Form data received:", data)

#         # Process form data
#         gender = 1 if data['Gender'] == 'male' else 0
#         age = float(data['Age'])
#         height = float(data['Height'])
#         weight = float(data['Weight'])
#         duration = float(data['Duration'])
#         heart_rate = float(data['Heart_Rate'])
#         body_temp = float(data['Body_Temp'])

#         # Model expects a 2D array
#         features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
#         prediction = model.predict(features)

#         return jsonify({'Calories_Burned': prediction[0]})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    print("Request method:", request.method)
    print("Request content type:", request.content_type)

    if model is None:
        return jsonify({"error": "Model not loaded!"}), 500

    try:
        # Parse JSON data from the request
        if request.is_json:
            data = request.get_json()
            print("JSON data received:", data)
        else:
            return jsonify({"error": "Invalid content type, JSON expected"}), 400

        # Extract and process data
        gender = 1 if data.get('Gender', '').lower() == 'male' else 0
        age = float(data['Age'])
        height = float(data['Height'])
        weight = float(data['Weight'])
        duration = float(data['Duration'])
        heart_rate = float(data['Heart_Rate'])
        body_temp = float(data['Body_Temp'])

        # Model expects a 2D array
        features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
        prediction = model.predict(features)

        # Convert NumPy float32 to Python float
        return jsonify({'Calories_Burned': float(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
