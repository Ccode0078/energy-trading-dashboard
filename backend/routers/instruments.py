from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.post("/insturments/", response_model=schemas.BaseModel)
async def create_instrument(instrument: schemas.InstrumentCreate, db: AsyncSession = Depends(get_db)):
    # create a models.Instrument object
   db_instrument = models.Instrument(**instrument.model_dump())
   db.add(db_instrument)
   db.commit()
   db.refresh(db_instrument)
   return db_instrument




    # add it to db
    # commit
    # refresh
    # return it
@router.get("/instruments", response_model=List[schemas.InstrumentResponse])
async def get_instruments(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Instrument))
    return result.scalars().all()