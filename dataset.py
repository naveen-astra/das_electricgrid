import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate synthetic sine waves (normal)
def generate_normal_data(num_samples=1000, length=100):
    x = np.linspace(0, 4*np.pi, length)
    return [np.sin(x) + np.random.normal(0, 0.1, length) for _ in range(num_samples)]

# Generate anomalies (spikes or sudden changes)
def generate_anomalies(num_samples=100, length=100):
    x = np.linspace(0, 4*np.pi, length)
    return [np.sin(x) + np.random.normal(0, 0.1, length) + np.random.uniform(-2, 2, length) for _ in range(num_samples)]

# Combine normal and anomaly data
normal_data = generate_normal_data()
anomaly_data = generate_anomalies()

X = np.array(normal_data + anomaly_data)
y = np.array([0] * len(normal_data) + [1] * len(anomaly_data))  # 0 = normal, 1 = anomaly

# Apply FFT
X_fft = np.abs(np.fft.fft(X, axis=1))

# Save as CSV
df = pd.DataFrame(X_fft)
df["label"] = y
df.to_csv("synthetic_data.csv", index=False)

print("✅ Synthetic data saved to synthetic_data.csv")
