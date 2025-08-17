from fastapi import APIRouter
from pydantic import BaseModel
import os, json, requests
from dotenv import load_dotenv

load_dotenv()
DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")

DROPBOX_FILE_PATH = "/assembled_finance_dataframe.json"
DROPBOX_API_URL = "https://content.dropboxapi.com/2/files/download"

router = APIRouter(prefix="/finance", tags=["Finance"])

class MultiQuery(BaseModel):
    contexts: list[str]

def load_finance_data():
    headers = {
        "Authorization": f"Bearer {DROPBOX_TOKEN}",
        "Dropbox-API-Arg": json.dumps({"path": DROPBOX_FILE_PATH})
    }
    response = requests.post(DROPBOX_API_URL, headers=headers)
    response.raise_for_status()
    return json.loads(response.content.decode("utf-8"))

@router.post("/search_multiple")
def search_multiple(query: MultiQuery):
    finance_data = load_finance_data()
    results = []
    for ctx in query.contexts:
        matched = [
            row for row in finance_data
            if str(row.get("transaction_id")) == ctx or str(row.get("patient_id")) == ctx
        ]
        matched_clean = [{k: v for k, v in row.items() if v not in [None, ""]} for row in matched]
        results.append({ctx: matched_clean if matched_clean else "No matching data found"})
    return results
