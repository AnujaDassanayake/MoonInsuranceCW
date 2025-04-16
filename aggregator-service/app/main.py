from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import logging

logging.basicConfig(level=logging.INFO)

from . import services, metrics, schemas
from .redshift_utils import push_to_redshift  # <-- Import the Redshift function

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Aggregator Service is Running"}

@app.get("/metrics/", response_model=schemas.MetricsResponse)
async def get_metrics():
    try:
        sales_data = await services.fetch_sales_data()
        metrics_result = metrics.calculate_metrics(sales_data)

        #debugging code
        logging.info("Calling push_to_redshift with metrics:")
        logging.info(metrics_result.top_agents)
        
        # Always push metrics to Redshift (even if no notification sent)
        push_to_redshift(metrics_result.top_agents)

        # Notification only if threshold met
        for agent in metrics_result.top_agents:
            if agent.total_sales > 100000:
                await services.send_notification(
                    f"🚀 Agent {agent.agent_code} exceeded sales target with ${agent.total_sales:,.2f}"
                )

        return metrics_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))