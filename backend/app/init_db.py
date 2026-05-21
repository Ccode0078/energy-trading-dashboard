import asyncio
from app.database import engine, Base
from app.models import Instrument

async def init_models():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Tables created successfully")
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(init_models())