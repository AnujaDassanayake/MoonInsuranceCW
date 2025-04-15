from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    agent_code = Column(String, index=True)
    product_name = Column(String)
    sale_amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
