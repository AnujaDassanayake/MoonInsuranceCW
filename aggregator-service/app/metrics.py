from collections import defaultdict
from typing import List
from . import schemas


def calculate_metrics(sales_data: List[schemas.Sale]) -> schemas.MetricsResponse:
    agent_sales_totals = defaultdict(float)
    product_sales_totals = defaultdict(float)

    # Aggregate Total Sales Per Agent and Product
    for sale in sales_data:
        agent_sales_totals[sale["agent_code"]] += sale["sale_amount"]
        product_sales_totals[sale["product_name"]] += sale["sale_amount"]

    # Prepare Top Agents List
    top_agents = [
        schemas.AgentSales(agent_code=agent, total_sales=total)
        for agent, total in sorted(agent_sales_totals.items(), key=lambda x: x[1], reverse=True)
    ]

    # Prepare Top Products List
    top_products = [
        schemas.ProductSales(product_name=product, total_sales=total)
        for product, total in sorted(product_sales_totals.items(), key=lambda x: x[1], reverse=True)
    ]

    return schemas.MetricsResponse(
        top_agents=top_agents,
        top_products=top_products
    )
