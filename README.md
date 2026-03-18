# krishimitra project
AI-Powered Crop Recommendation System
<br>
​📌 Project Overview
​This project is a Machine Learning-based Decision Support System designed for agricultural planning at the Village Panchayat level. It helps farmers and local authorities identify the most suitable crop to grow based on specific soil and environmental conditions.
​The system uses a Random Forest Classifier trained on a dataset of 22,000+ records to provide highly accurate recommendations, aiming to optimize crop yield and promote sustainable farming.

​🚀 Key Features
​Google-Grade Data Pipeline: Includes automated outlier detection using the IQR method and data standardization.
​High Accuracy: Achieving 99.19% accuracy using an optimized Random Forest ensemble model.
​Hybrid Architecture: AI Engine: Python (Flask)
​Backend: Java (Spring Boot)
​Frontend: React.js
​Professional Persistence: Uses Pickle to serialize both the trained model and the StandardScaler to ensure consistent predictions in production.

# Data Science Workflow
​Exploratory Data Analysis (EDA): Checking for null values and data distribution.
​Preprocessing: Removing outliers and scaling features (N, P, K, Temp, Humidity, pH, Rainfall).
​Model Training: Training a 100-tree Random Forest with stratified splits.
​Serialization: Packaging the model and scaler into a .pkl file for real-time API usage.

​🔌 API Endpoints
​POST /predict
​Input: Soil and Weather JSON (N, P, K, etc.)
​Output: { "status": "success", "crop": "Rice" }
​👨‍💻 How to Run
​Install dependencies: pip install -r requirements.txt
​Run the AI server: python app.py
​The API will be live at http://localhost:5000

