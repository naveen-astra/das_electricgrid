# DAS-based Electric Grid Monitoring System

## Overview
This repository implements a **Distributed Acoustic Sensing (DAS)**-based monitoring system for electric power grids. The system uses a laser and photodiode interfaced with an Arduino to detect vibrations along power lines. Vibration data is transmitted to the cloud, processed with Fast Fourier Transform (FFT) for frequency analysis, and fed into a Long Short-Term Memory (LSTM) neural network for anomaly detection — enabling proactive fault prediction and instant alerting.

## Key Features
- Real-time vibration detection using laser-photodiode DAS setup
- Cloud data ingestion and storage
- FFT-based frequency-domain signal analysis
- LSTM model for anomaly/fault detection
- Automated alerting system
- Scalable design for distributed grid monitoring

## Technologies Used
- **Hardware, Hardware**: Arduino, Laser module, Photodiode
- **Languages**: C++ (Arduino), Python
- **Libraries**: NumPy, SciPy (FFT), TensorFlow/Keras (LSTM), Matplotlib/Plotly
- **Communication**: MQTT / REST for cloud upload
- **Optional Cloud**: AWS IoT, Google Cloud IoT, or Firebase

## Project Structuredas_electricgrid
├── hardware/
│   ├── arduino_sketch/      # Arduino .ino firmware
│   └── schematics/          # Wiring diagrams
├── software/
│   ├── data_ingestion/      # Cloud upload scripts
│   ├── signal_processing/   # FFT analysis
│   ├── ml_model/            # LSTM training & inference
│   └── visualization/       # Real-time dashboard (Streamlit/Dash)
├── datasets/                # Sample vibration data
├── docs/                    # Additional documentation
└── README.md



## Quick Start
1. Flash the Arduino with code from `hardware/arduino_sketch/`
2. Run data ingestion script: `python software/data_ingestion/upload.py`
3. Train/predict with LSTM: Open notebooks in `software/ml_model/`
4. Launch dashboard: `streamlit run software/visualization/app.py`

