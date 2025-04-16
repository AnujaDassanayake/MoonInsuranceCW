import logging
import psycopg2
import os

def push_to_redshift(metrics):
    """
    Dummy function to simulate pushing data to Redshift.

    Args:
        metrics: List of objects with 'agent_code' and 'total_sales'
    """
    logging.info("🚀 [SIMULATION] Would push the following data to Redshift:")

    for metric in metrics:
        print(f"  - Agent: {metric.agent_code}, Sales: {metric.total_sales}")
        logging.info(f"  - Agent: {metric.agent_code}, Sales: {metric.total_sales}")


# def push_to_redshift(metrics):
#     """
#     Insert aggregated metrics into Redshift table.

#     Args:
#         metrics: List of objects with 'agent_code' and 'total_sales'
#     """

#     # Read Redshift connection details from environment variables
#     redshift_host = os.getenv("REDSHIFT_HOST")
#     redshift_db = os.getenv("REDSHIFT_DB")
#     redshift_user = os.getenv("REDSHIFT_USER")
#     redshift_password = os.getenv("REDSHIFT_PASSWORD")
#     redshift_port = 5439  # Default Redshift port

#     # Establish connection
#     conn = psycopg2.connect(
#         host=redshift_host,
#         dbname=redshift_db,
#         user=redshift_user,
#         password=redshift_password,
#         port=redshift_port
#     )

#     cur = conn.cursor()

#     insert_query = "INSERT INTO sales_metrics (agent_code, total_sales) VALUES (%s, %s)"

#     for metric in metrics:
#         cur.execute(insert_query, (metric.agent_code, metric.total_sales))

#     conn.commit()
#     cur.close()
#     conn.close()

#     print("✅ Data pushed to Redshift successfully!")
