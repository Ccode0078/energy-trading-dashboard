from pydantic import BaseModel, ConfigDict



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