import streamlit as st
import requests

# Define the URL where our FastAPI backend is running locally
# When we move to Docker later, this URL will change dynamically!
BACKEND_URL = "http://backend-api:8000/predict"

cluster_actions = {
    0: {
        "name": "Loyal Customers",
        "action": """
        • Reward them with exclusive offers  
        • Provide early access to sale  
        • Encourage referrals  
        """
    },
    1: {
        "name": "At-Risk Customers",
        "action": """
        • Send re-engagement campaigns  
        • Provide personalized discounts  
        • Remind them of abandoned carts  
        """
    },
    2: {
        "name": "VIP Customers",
        "action": """
        • Provide premium support  
        • Offer high-value loyalty programs  
        • Prioritize them for new launches  
        """
    }
}

st.title("🛍️ RFM Customer Segmentation")
st.write("Predict customer segment via our production FastAPI engine.")

with st.form("rfm_form"):
    recency = st.number_input("Recency (days since last purchase)", min_value=1, value=30, help="Number of days since the customer's last purchase. Lower = more recent.")
    frequency = st.number_input("Frequency (number of purchases)", min_value=0, value=5, help="Total number of purchases the customer made. Higher = more loyal.")
    monetary = st.number_input("Monetary Value (total spend)", value=5000.0, help="Total amount the customer has spent. Higher = more valuable.")

    submitted = st.form_submit_button("Predict Segment")

if submitted:
    # 1. Package up the inputs into a payload matching our Pydantic schema exactly
    payload = {
        "recency": int(recency),
        "frequency": int(frequency),
        "monetary": float(monetary)
    }

    try:
        # 2. Make an HTTP POST request to the FastAPI backend
        with st.spinner("Communicating with backend API engine..."):
            response = requests.post(BACKEND_URL, json=payload, timeout=5)
        
        # 3. Handle the response
        if response.status_code == 200:
            # Parse out the JSON results sent back from FastAPI
            result = response.json()
            cluster = result["cluster"]
            segment_name = result["segment_name"]

            st.success(f"### 🏷 Customer Segment: **{segment_name}** (Cluster {cluster})")
            st.markdown("#### 📌 Recommended Business Actions:")
            st.write(cluster_actions[cluster]['action'])
        else:
            st.error(f"❌ Backend returned an error status: {response.status_code}")
            st.json(response.json())

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI backend. Is your Uvicorn server running?")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {str(e)}")