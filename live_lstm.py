import requests
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense
import os
import time
from send_alerts import send_email_alert

# ThingSpeak API Keys
THINGSPEAK_CHANNEL_ID = "2865842"
THINGSPEAK_READ_API_KEY = "JL7PFJR3707OBUQJ"

# Load or Initialize Model
MODEL_PATH = "lstm_model.h5"
if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
else:
    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=(10, 1)),  # 10 time steps
        LSTM(64),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.save(MODEL_PATH)

# Training Data Storage
training_data = []
labels = []

def fetch_data():
    """Fetch latest 10 strain sensor values from ThingSpeak"""
    url = f"https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/fields/1.json?results=10&api_key={THINGSPEAK_READ_API_KEY}"
    response = requests.get(url).json()
    
    if "feeds" not in response:
        return np.zeros(10)  # Return zeros if API fails
    
    values = [float(feed["field1"]) if feed["field1"] else 0 for feed in response["feeds"]]
    return np.array(values)

def retrain_model():
    """Retrain LSTM model on accumulated live data"""
    global training_data, labels
    
    if len(training_data) < 50:  # Wait until at least 50 samples collected
        return
    
    X_train = np.array(training_data)
    y_train = np.array(labels)

    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)  # Reshape for LSTM

    model.fit(X_train, y_train, epochs=3, batch_size=8, verbose=0)  # Quick retrain
    model.save(MODEL_PATH)  # Save updated model
    print("✅ Model retrained and saved.")

def detect_anomaly():
    """Fetch live data, apply FFT, detect anomalies, and send alerts"""
    global training_data, labels

    raw_data = fetch_data()
    fft_features = np.abs(np.fft.fft(raw_data)).reshape(1, -1, 1)

    prediction = model.predict(fft_features)[0][0]
    print(f"🔍 Prediction Score: {prediction:.4f}")

    # Append new data to training dataset
    training_data.append(raw_data)
    labels.append(1 if prediction > 0.7 else 0)

    # Retrain model every 10 iterations
    if len(training_data) % 10 == 0:
        retrain_model()

    if prediction > 0.02:
        print("🚨 Anomaly Detected! Sending alerts...")
        send_email_alert()

if __name__ == "__main__":
    print("🚀 Running Continuous Training & Anomaly Detection...")
    while True:
        detect_anomaly()
        time.sleep(2)
