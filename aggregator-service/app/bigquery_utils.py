from google.cloud import bigquery
from datetime import datetime
import os

def push_to_bigquery(agent_sales: list):
    """
    Push aggregated agent sales to BigQuery.
    """
    project_id = os.getenv("GCP_PROJECT_ID")  # e.g., mooninsuarancecw
    dataset_id = os.getenv("BQ_DATASET", "mooninsurance_metrics")
    table_id = os.getenv("BQ_TABLE", "top_agent_sales")
    full_table_id = f"{project_id}.{dataset_id}.{table_id}"

    client = bigquery.Client()

    rows = [
        {
            "agent_code": agent.agent_code,
            "total_sales": agent.total_sales,
            "timestamp": datetime.utcnow(),  # ✅ Add timestamp
        }
        for agent in agent_sales
    ]

    errors = client.insert_rows_json(full_table_id, rows)
    if errors:
        print("❌ Failed to insert rows:", errors)
    else:
        print(f"✅ Successfully pushed {len(rows)} rows to BigQuery.")
