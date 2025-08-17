import streamlit as st
import requests
import uvicorn
import threading
from fastapi import FastAPI

from patients_api import router as patients_router
from finance_api import router as finance_router
from staff_api import router as staff_router

app = FastAPI(title="Unified API")
app.include_router(patients_router)
app.include_router(finance_router)
app.include_router(staff_router)

def run_backend():
    uvicorn.run(app, host="127.0.0.1", port=8008, log_level="info")

threading.Thread(target=run_backend, daemon=True).start()

st.title("Unified Data Search (Centralized)")

API_ENDPOINTS = {
    "Patients": "http://127.0.0.1:8008/patients/search_multiple",
    "Staff": "http://127.0.0.1:8008/staff/search_multiple",
    "Finance": "http://127.0.0.1:8008/finance/search_multiple"
}

option = st.radio("Choose dataset:", list(API_ENDPOINTS.keys()))

if option == "Patients":
    label = "Enter patient_id:"
elif option == "Staff":
    label = "Enter staff_id:"
else:
    label = "Enter transaction_id:"

contexts_input = st.text_area(f"{label} (one per line)")
contexts = [line.strip() for line in contexts_input.split("\n") if line.strip()]

if st.button("Search"):
    if not contexts_input.strip():
        st.error("Please enter a valid ID")
    else:
        try:
            response = requests.post(API_ENDPOINTS[option], json={"contexts": contexts}, timeout=30)
            response.raise_for_status()
            results = response.json()
            if not results:
                st.info("No matching data found.")
            else:
                for item in results:
                    for key, val in item.items():
                        st.subheader(f"Query: {key}")
                        st.json(val)
        except requests.exceptions.RequestException as e:
            st.error(f"Something went wrong while fetching data: \n{e}")
        except Exception as e:
            st.error(f"I guess something went wrong: \n{e}")

# Run this file only: `streamlit run frontend.py`

