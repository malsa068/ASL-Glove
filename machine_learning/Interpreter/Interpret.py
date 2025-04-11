import serial
import numpy as np
import pandas as pd 
import joblib
from collections import Counter
import os
print("Current working directory:", os.getcwd())

#ensures that the pkl files are read without having to specifically declare path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_pkl = os.path.join(BASE_DIR, "gesture_model.pkl")
scaler_pkl = os.path.join(BASE_DIR, "scaler.pkl")
encoder_pkl = os.path.join(BASE_DIR, "label_encoder.pkl")

model = joblib.load(model_pkl)
scaler = joblib.load(scaler_pkl)
encoder = joblib.load(encoder_pkl)

ser = serial.Serial('COM4', 9600) 
print("Model input dtype check:")
print(type(model))
print("Number of features:", model.n_features_in_)
print("First tree type check:", type(model.estimators_[0].tree_.threshold))
print("Tree threshold dtype:", model.estimators_[0].tree_.threshold.dtype)


def predict_voted_gesture(rf_model, scaler, encoder, sensor_input_raw):

    try:
        # 1. Convert to float32 array
        sensor_input_array = np.array(sensor_input_raw, dtype=np.float32).reshape(1, -1)
        print("Input dtype:", sensor_input_array.dtype)

        # 2. Convert to DataFrame with proper column names
        sensor_input_df = pd.DataFrame(sensor_input_array, columns=scaler.feature_names_in_)

        # 3. Scale input
        scaled_input = scaler.transform(sensor_input_df)
        print("Scaled input dtype:", scaled_input.dtype)

        # 4. Predict using individual trees
        votes = []
        for i, tree in enumerate(rf_model.estimators_):
            pred = tree.predict(scaled_input.astype(np.float32))[0]  # force float32 again
            pred_label = encoder.inverse_transform([int(pred)])[0]  # make sure prediction is int
            votes.append(pred_label)

        # 5. Voting logic
        vote_counts = Counter(votes)
        print("Votes:", vote_counts)
        most_common = vote_counts.most_common(1)[0]
        return most_common[0] if most_common[1] >= 2 else "Unknown"

    except Exception as e:
        print("❌ Error inside predict_voted_gesture:", e)
        return "Error"

while True:
    line = ser.readline().decode('utf-8').strip()
    print(f"Raw line from glove: '{line}'")
    
    
    # Skip any lines that aren't valid sensor data
    if not any(char.isdigit() for char in line) or "Initializing" in line:
        print("Ignored:", line)
        continue

    try:
        parts = [float(x.strip()) for x in line.split(",")]
        if len(parts) == 8:
            gesture = predict_voted_gesture(model, scaler, encoder, parts)
            print("🖐 Gesture Detected:", gesture)
        else:
            print("⚠️ Invalid data format:", line)
    except Exception as e:
        print("❌ Error:", e)


