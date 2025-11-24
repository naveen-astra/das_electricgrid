import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import os

# Load synthetic FFT data
df = pd.read_csv("synthetic_data.csv")
X_train = df.iloc[:, :-1].values  # FFT features
y_train = df["label"].values  # Labels

# Reshape for LSTM (samples, time_steps, features)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)

# Define LSTM model
model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    LSTM(64),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Save model
os.makedirs("../models", exist_ok=True)
model.save("lstm_model.h5")
print("✅ Model saved as lstm_model.h5")
