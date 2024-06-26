import numpy as np
from keras.models import load_model
from models.normalize import scaler
from flask import Flask, jsonify, request, abort
from dotenv import load_dotenv
import sys
import os

load_dotenv()

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Specify the port number
PORT = os.getenv('PORT') or 3000

# Specify the absolute path to the model file
current_path = os.getcwd()
model_file_path = current_path + '/model.keras'

# Load the model
model = load_model(model_file_path)

# Create a Flask app
app = Flask(__name__)


def process_form_data(form):
    """Process form data and return a numpy array."""
    try:
        gender = '1' if form['gender'] == 'true' else '0'
        met = '0' if form['met'] == 'true' else '1'
        income = int(form['income']) * 0.57 * 1.52  # inflation + purchasing power parity
        data = [gender, int(form['age']), income, int(form['career']), int(form['attr']),
                int(form['sinc']), int(form['intel']), int(form['fun']), int(form['amb']),
                int(form['shar']), met]
        return np.array(data).reshape(1, -1)
    except KeyError:
        abort(400, description="Required form data not provided.")


@app.route('/predict', methods=['POST'])
def predict():
    """Predict the outcome based on the provided form data."""
    if request.method == 'POST':
        data = process_form_data(request.form)
        data = scaler.transform(data)
        prediction = model.predict(data)
        return jsonify({'prediction': round(prediction[0][0], 2) * 100})


if __name__ == '__main__':
    app.run(port=PORT)
