from fastapi import FastAPI, HTTPException
from . import services, metrics, schemas

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Aggregator Service is Running"}

@app.get("/metrics/", response_model=schemas.MetricsResponse)
async def get_metrics():
    try:
        sales_data = await services.fetch_sales_data()
        metrics_result = metrics.calculate_metrics(sales_data)

        # 🚨 Trigger notification if any agent exceeds 100000 in sales
        for agent in metrics_result.top_agents:
            if agent.total_sales > 100000:
                await services.send_notification(
                    f"🚀 Agent {agent.agent_code} exceeded sales target with ${agent.total_sales:,.2f}"
                )

        return metrics_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
