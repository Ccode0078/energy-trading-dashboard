from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.database import get_db
from app import models, schemas


router = APIRouter()

@router.post("/trades", response_model=schemas.TradeResponse)
async def create_trade(trade: schemas.TradeCreate, db: AsyncSession = Depends(get_db)):
    db_trade = models.Trade(**trade.model_dump())
    db.add(db_trade)
    await db.commit()
    await db.refresh(db_trade)
    return db_trade

@router.get("/trades", response_model=List[schemas.TradeResponse])
async def get_trades(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Trade))
    return result.scalars().all()
   