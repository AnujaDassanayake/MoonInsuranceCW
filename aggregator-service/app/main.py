import asyncio
from app import services, metrics
from app.redshift_utils import push_to_redshift

async def run_job():
    try:
        print("🚀 Aggregator CronJob started")

        # Step 1: Fetch sales data from Integration Service
        sales_data = await services.fetch_sales_data()

        # Step 2: Calculate metrics
        metrics_result = metrics.calculate_metrics(sales_data)

        # Step 3: Push metrics to Redshift
        push_to_redshift(metrics_result.top_agents)

        # Step 4: Send notifications if needed
        for agent in metrics_result.top_agents:
            if agent.total_sales > 100000:
                await services.send_notification(
                    f"🚨 Agent {agent.agent_code} exceeded sales target with ${agent.total_sales:,.2f}"
                )

        print("✅ Aggregation job completed successfully.")

    except Exception as e:
        print(f"❌ Job failed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(run_job())
