from ecommerce_integrations.shopify.constants import EVENT_MAPPER
from ecommerce_integrations.shopify.order import sync_sales_order
from ecommerce_integrations.shopify.utils import create_shopify_log

import frappe


def process_request1(data, event):
    # create log
    log = create_shopify_log(method=EVENT_MAPPER[event], request_data=data)
    sync_sales_order(data, log.name)
    # enqueue backround job
    # frappe.enqueue(
    #     method=EVENT_MAPPER[event],
    #     queue="short",
    #     timeout=300,
    #     is_async=True,
    #     **{"payload": data, "request_id": log.name},
    # )
