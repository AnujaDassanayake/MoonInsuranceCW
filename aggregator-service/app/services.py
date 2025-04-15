import httpx
from typing import List
from . import schemas

INTEGRATION_SERVICE_URL = "http://localhost:8000/sales/"  # Change in prod

async def fetch_sales_data() -> List[schemas.Sale]:
    async with httpx.AsyncClient() as client:
        response = await client.get(INTEGRATION_SERVICE_URL)
        response.raise_for_status()  # Raise error if API fails
        sales_data = response.json()
        return sales_data
