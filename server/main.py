import numpy as np
from keras.src.saving import load_model
from models.normalize import scaler

model = load_model('model.keras')

# gender age income career attr sinc intel fun amb shar prob met
data = [1, 27, 250, 14, 6, 10, 10, 7, 8, 5, 8, 1]
data = np.array(data).reshape(1, -1)
data = scaler.transform(data)
prediction = model.predict(data)
print(f'Prediction: {prediction[0][0]:.2f}')

