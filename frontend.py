import streamlit as st
import requests
import time
import streamlit_extras.badges as badge

# This is my render deployed API-LINK  
API_URL = "https://fast-api-patient-insurance-by-chatak.onrender.com/predict" 

st.title("Insurance Premium Category Predictor by Chatak Shweta ")


with st.sidebar:
    st.markdown("### Connect with me")
    col1, col2 = st.columns(2)
    with col1:
        try:
            badge(type="github", name="shwetank-maurya")
        except:
            st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Shwetank-blue?logo=github)](https://github.com/shwetank-maurya)")
        try:
            badge(type="kaggle", name="shwetank_maurya")
        except:
            st.markdown("[![kaggle](https://img.shields.io/badge/kaggle-Shwetank-pink?logo=kaggle)](https://www.kaggle.com/shwetankmaurya)")
    with col2:
        try:
            badge(type="medium", name="shwetank_maurya")
        except:
            st.markdown("[![medium](https://img.shields.io/badge/Medium-Shwetank-blue?logo=medium)](https://medium.com/@shwetank_maurya)")
st.markdown("""
<div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #4e73df; margin-bottom: 30px;'>
    <h4 style='color: #2e3a59; margin-top: 0;'>Provide the data and It'll provide you the outputs about the insurance probabilty</h4>
    <p style='color: #6c757d; margin-bottom: 0;'>
        Don't think this as a line on stone 'cause Model is trained on dummy data...
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("Enter your details below:")
        
colu1,colu2,colu3=st.columns(3)
with colu1:
    age = st.number_input("Age", min_value=1, max_value=119, value=30)
    weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
with colu2:
    height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
    income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
with colu3:
    smoker = st.selectbox("Are you a smoker?", options=[True, False])
    city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        with st.status("Getting Response...", expanded=True) as status:
            st.write("Connencting API...")
            time.sleep(2)
            st.write("Connected API...")
            time.sleep(1)
            st.write("Response...")
            time.sleep(1)
            status.update(
                label="Download complete!", state="complete", expanded=True
                 )
            response = requests.post(API_URL, json=input_data)
            result = response.json()
            
            st.write('-'*40)
            
            if response.status_code == 200 and "predicted_category" in result:
                prediction = result["predicted_category"]
                st.success(f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**")
                st.write("🔍 Confidence:", prediction["confidence"])
            
                st.write(" Class Probabilities:")
                st.json(prediction["class_probabilities"])

            else:
                st.error(f"API Error: {response.status_code}")
                st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")