import streamlit as st
import requests

# 🔹 Update with your deployed FastAPI URL
BACKEND_URL = "https://api.langflow.astra.datastax.com/lf/c3820c28-e6fb-4643-a56e-6555ba30df67/api/v1/run/ArogyaMantra"

st.title("🩺 Arogya Mitra")

st.markdown("### 📋 Patient Demographics")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.text_input("Weight (Optional)")
height = st.text_input("Height (Optional)")
medical_history = st.text_area("Medical History")
lifestyle_factors = st.text_area("Lifestyle Factors (Optional)")

st.markdown("### 🤒 Symptoms")
primary_symptom = st.text_input("Primary Symptom")
duration = st.text_input("Duration")
severity = st.selectbox("Severity", ["Mild", "Moderate", "Severe"])
associated_symptoms = st.text_area("Associated Symptoms (Optional)")

st.markdown("### ❤️ Vital Signs")
body_temperature = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, step=0.1)
heart_rate = st.text_input("Heart Rate (Optional)")
blood_pressure = st.text_input("Blood Pressure")

st.markdown("### 🌎 Contextual Information")
recent_travel = st.text_input("Recent Travel (Optional)")
allergies = st.text_area("Allergies")
medications = st.text_area("Current Medications")
patient_email = st.text_input("Your Email (For Reports)")

# 🔹 Submit Button
if st.button("🔍 Analyze Health Condition"):
    data = {
        "age": age, "gender": gender, "weight": weight, "height": height,
        "medical_history": medical_history, "lifestyle_factors": lifestyle_factors,
        "primary_symptom": primary_symptom, "duration": duration, "severity": severity,
        "associated_symptoms": associated_symptoms, "body_temperature": body_temperature,
        "heart_rate": heart_rate, "blood_pressure": blood_pressure,
        "recent_travel": recent_travel, "allergies": allergies,
        "medications": medications, "patient_email": patient_email
    }

    try:
        response = requests.post(BACKEND_URL, json=data)
        result = response.json()

        st.markdown("## 🏥 Analysis Result")
        st.write(f"**Severity:** {result['severity']}")
        st.write(f"**Recommended Remedies:** {result['remedies']}")
        st.write(f"**Medications:** {result['medications']}")

        if result["doctor"]:
            st.warning(f"📞 Consult **Dr. {result['doctor']}** at **{result['doctor_email']}**")

    except Exception as e:
        st.error("⚠ Error connecting to backend. Please try again.")
