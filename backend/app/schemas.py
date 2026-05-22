from pydantic import BaseModel, ConfigDict
from datetime import datetime



class InstrumentCreate(BaseModel):
    symbol: str
    name: str
    commodity_type: str
    unit: str



    model_config = ConfigDict(from_attributes=True)



class InstrumentResponse(BaseModel):
    id: int
    symbol: str
    name: str
    commodity_type: str
    unit: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class TradeCreate(BaseModel):
    instrument_id: int
    side: str
    quantity: float
    price: float
    book: str

    model_config = ConfigDict(from_attributes=True)





class TradeResponse(BaseModel):
    id: int
    instrument_id: int
    side: str
    quantity: float
    price: float
    book: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

