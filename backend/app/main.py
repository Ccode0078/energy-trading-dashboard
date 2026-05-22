from fastapi import FastAPI
from app.routers import instruments

app = FastAPI()

app.include_router(instruments.router)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "energy-trading-api"}
