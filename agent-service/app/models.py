from .database import Base
from sqlalchemy import Column, Integer, String

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String)
    product = Column(String)  # comma separated list of products
