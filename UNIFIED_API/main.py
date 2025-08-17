from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from self_patients_api import app as patients_app
from self_finance_api import app as finance_app
from self_staff_api import app as staff_app

app = FastAPI(title="UNIFIED_API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/patients", patients_app)
app.mount("/finance", finance_app)
app.mount("/staff", staff_app)
