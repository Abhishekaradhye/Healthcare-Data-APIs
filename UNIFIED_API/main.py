from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from patients_api import router as patients_router
from finance_api import router as finance_router
from staff_api import router as staff_router

app = FastAPI(title="UNIFIED_API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ include the routers instead of mount
app.include_router(patients_router)
app.include_router(finance_router)
app.include_router(staff_router)
