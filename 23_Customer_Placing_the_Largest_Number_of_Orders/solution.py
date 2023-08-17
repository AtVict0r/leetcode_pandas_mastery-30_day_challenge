import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = orders.groupby('customer_number')['order_number'].count().reset_index()
    mask = result['order_number'] == result['order_number'].max()
    return result[mask][['customer_number']]