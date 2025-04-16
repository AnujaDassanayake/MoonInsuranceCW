import httpx
from typing import List
from . import schemas

INTEGRATION_SERVICE_URL = "http://integration-service/sales/"

async def fetch_sales_data() -> List[schemas.Sale]:
    async with httpx.AsyncClient() as client:
        response = await client.get(INTEGRATION_SERVICE_URL)
        response.raise_for_status()  # Raise error if API fails
        sales_data = response.json()
        return sales_data

async def send_notification(message: str):
    notify_url = "http://localhost:8002/notify/"
    async with httpx.AsyncClient() as client:
        response = await client.post(notify_url, json={"message": message})
        response.raise_for_status()
