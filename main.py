from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Nova API Starter", version="1.0.0")

class HealthStatus(BaseModel):
    status: str
    version: str

@app.get("/health", response_model=HealthStatus)
def health_check():
    """
    Nova API Health Endpoint
    Provides standard system checks.
    """
    return HealthStatus(status="OK", version="1.0.0")
