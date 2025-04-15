from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import services, metrics, schemas
from .redshift_utils import push_to_redshift  # <-- Import the Redshift function

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Aggregator Service is Running"}

@app.get("/metrics/", response_model=schemas.MetricsResponse)
async def get_metrics():
    try:
        # Step 1: Fetch sales data from Integration Service
        sales_data = await services.fetch_sales_data()

        # Step 2: Calculate metrics
        metrics_result = metrics.calculate_metrics(sales_data)

        # Step 3: Push Aggregated Metrics to Redshift
        push_to_redshift(metrics_result.top_agents)

        # Step 4: Send Notification if Sales Threshold Crossed
        for agent in metrics_result.top_agents:
            if agent.total_sales > 100000:
                await services.send_notification(
                    f"🚀 Agent {agent.agent_code} exceeded sales target with ${agent.total_sales:,.2f}"
                )

        return metrics_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
