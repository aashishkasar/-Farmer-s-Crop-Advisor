import streamlit as st
import numpy as np
import pickle

# Load the trained model and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Crop dictionary mapping predictions to crop names
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

# Streamlit app
st.set_page_config(page_title="Farmer Crop Advisor", page_icon="🌾", layout="centered")

# Main title
st.title("🌾 Farmer's Crop Advisor")
st.markdown(
    """
    **Welcome to the Crop Recommendation System!**  
    Provide the environmental and soil parameters below to get the best crop recommendation for cultivation.
    """
)

# Form for user input
with st.form("crop_input_form"):
    st.subheader("Enter the following details:")
    
    N = st.number_input("Nitrogen (N)", min_value=0, max_value=500, value=0, step=1)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=500, value=0, step=1)
    K = st.number_input("Potassium (K)", min_value=0, max_value=500, value=0, step=1)
    temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0, step=0.1)

    # Submit button
    submitted = st.form_submit_button("Get Recommendation")

# Handle form submission
if submitted:
    # Collect inputs and preprocess
    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    # Get crop recommendation
    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        st.success(f"✅ {crop} is the best crop to be cultivated with the provided data.")
    else:
        st.error("❌ Sorry, we could not determine the best crop to be cultivated with the provided data.")

# Footer
st.markdown(
    """
    ---
    © 2025 Developed by **Aashish** | Dedicated to **Farmers** 🌾
    """
)
