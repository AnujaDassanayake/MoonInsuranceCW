from pydantic import BaseModel
from datetime import datetime


class SaleCreate(BaseModel):
    agent_code: str
    product_name: str
    sale_amount: float


class Sale(SaleCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True  # Pydantic V2 equivalent of orm_mode
