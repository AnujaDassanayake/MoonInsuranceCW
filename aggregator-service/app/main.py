from fastapi import FastAPI, HTTPException
from . import services, metrics, schemas
from typing import List

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Aggregator Service is Running"}


@app.get("/metrics/", response_model=schemas.MetricsResponse)
async def get_metrics():
    try:
        sales_data = await services.fetch_sales_data()
        metrics_result = metrics.calculate_metrics(sales_data)
        return metrics_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
