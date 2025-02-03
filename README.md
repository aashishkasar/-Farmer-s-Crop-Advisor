# Crop Recommendation System

This project is a **Flask-based web application** that helps farmers determine the most suitable crop to grow based on specific soil and environmental conditions.

---

## Features
- **User-Friendly Interface**: Provides an intuitive form for entering soil and environmental parameters.
- **Dynamic Crop Recommendation**: Uses a machine learning model to predict the best crop.
- **Responsive Design**: Optimized for mobile and desktop views using Bootstrap.
- **Search Functionality**: Allows users to search for specific crops.
- **User Authentication**: Includes a farmer login and logout system.

---

## Flask Environment Setup

### Prerequisites
1. Python (>= 3.7)
2. Virtual Environment (optional but recommended)

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/crop-recommendation-system.git
   cd crop-recommendation-system
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   flask run
   ```
   The application will be available at `http://127.0.0.1:5000`.

---

## Sample Input Table
Below are the input parameters required for the crop recommendation system:

| Parameter      | Description                 | Example Value |
|----------------|-----------------------------|---------------|
| Nitrogen (N)   | Content of nitrogen in soil | 90            |
| Phosphorus (P) | Content of phosphorus       | 42            |
| Potassium (K)  | Content of potassium        | 43            |
| Temperature (°C)| Atmospheric temperature   | 23.5          |
| Humidity (%)   | Percentage of humidity      | 80.2          |
| Soil pH        | Acidity or alkalinity of soil | 6.5          |
| Rainfall (mm)  | Average rainfall in mm      | 200.3         |

---

## Crop Chart
The table below provides a general guideline for suitable crops based on various soil and environmental conditions:

| Crop         | Ideal Nitrogen (N) | Ideal Phosphorus (P) | Ideal Potassium (K) | Temperature (°C) | Humidity (%) | Soil pH | Rainfall (mm) |
|--------------|---------------------|-----------------------|----------------------|-------------------|--------------|---------|---------------|
| Rice         | 80-120             | 40-60                | 20-30               | 20-35            | 70-90        | 5.0-6.5 | 150-300       |
| Wheat        | 60-100             | 30-50                | 30-40               | 15-25            | 60-80        | 6.0-7.0 | 100-200       |
| Maize        | 90-120             | 50-70                | 40-60               | 18-27            | 50-80        | 5.5-7.0 | 120-250       |
| Cotton       | 50-80              | 30-50                | 20-40               | 25-35            | 50-70        | 6.0-7.5 | 200-300       |
| Sugarcane    | 100-150            | 40-60                | 60-80               | 20-30            | 60-90        | 6.5-7.5 | 150-250       |
| Tomato       | 50-100             | 20-40                | 30-50               | 20-30            | 60-80        | 5.5-6.8 | 100-200       |
| Potato       | 80-120             | 40-60                | 50-70               | 15-25            | 70-85        | 5.0-6.0 | 120-200       |

---

## File Structure
```
├── app.py                 # Main Flask application file
├── templates/             # HTML templates
│   ├── index.html         # Main UI for crop recommendation
│   ├── about.html         # About page
│   └── contact.html       # Contact page
├── static/                # Static assets (CSS, JS, images)
├── model/                 # Directory for ML model
│   └── crop_model.pkl     # Pre-trained ML model file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## How It Works
1. User inputs parameters such as Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Soil pH, and Rainfall.
2. These values are sent to the Flask backend.
3. The backend loads a pre-trained machine learning model (e.g., Random Forest).
4. The model predicts the most suitable crop based on the input data.
5. The result is displayed to the user on the same page.

---

🚀 Successfully resolved sklearn & numpy import errors and ensured a smooth deployment! 🛠️
🔍 Fixed ComplexWarning and distutils issues by managing dependencies properly.
📌 Generated a clean requirements.txt for seamless environment setup.
✅ Debugged and optimized model loading with pickle & scikit-learn.

---

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or features.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- Developed by **Aashish**.
- Dedicated to the hardworking farmers of the world.
- Inspired by the mission to improve agricultural productivity through technology.

