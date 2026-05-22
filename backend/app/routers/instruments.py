from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.post("/instruments", response_model=schemas.InstrumentResponse)
async def create_instrument(instrument: schemas.InstrumentCreate, db: AsyncSession = Depends(get_db)):
    db_instrument = models.Instrument(**instrument.model_dump())
    db.add(db_instrument)
    await db.commit()
    await db.refresh(db_instrument)
    return db_instrument

@router.get("/instruments", response_model=List[schemas.InstrumentResponse])
async def get_instruments(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Instrument))
    return result.scalars().all()