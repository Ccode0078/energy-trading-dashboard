from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers import instruments, trades
import traceback

app = FastAPI()

app.include_router(instruments.router)
app.include_router(trades.router)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    traceback.print_exc()
    return JSONResponse(status_code=500, content={"detail": str(exc)})

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "energy-trading-api"}