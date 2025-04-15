from pydantic import BaseModel
from datetime import datetime
from typing import List


# Data fetched from Integration Service
class Sale(BaseModel):
    id: int
    agent_code: str
    product_name: str
    sale_amount: float
    timestamp: datetime


# Metrics Aggregation Output
class AgentSales(BaseModel):
    agent_code: str
    total_sales: float


class ProductSales(BaseModel):
    product_name: str
    total_sales: float


class MetricsResponse(BaseModel):
    top_agents: List[AgentSales]
    top_products: List[ProductSales]
