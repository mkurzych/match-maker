import numpy as np
from keras.src.saving import load_model
from models.normalize import scaler
from flask import Flask, jsonify, request

PORT = 5000

model = load_model('model.keras')

# gender age income career attr sinc intel fun amb met
# data = [1, 27, 250, 14, 6, 10, 10, 7, 5, 1]
# 1, 20, 500, 9, 7, 7, 7, 7, 8, 0

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form['data'].split(',')
        data = np.array(data).reshape(1, -1)
        data = scaler.transform(data)
        prediction = model.predict(data)
        return jsonify({'prediction': round(prediction[0][0], 2) * 100})


if __name__ == '__main__':
    app.run(port=PORT)

