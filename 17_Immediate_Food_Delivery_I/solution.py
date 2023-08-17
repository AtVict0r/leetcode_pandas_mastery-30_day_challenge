import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    mask = delivery['order_date'] == delivery['customer_pref_delivery_date']
    immediate_percent = (delivery[mask].size / delivery.size) * 100
    return pd.DataFrame({'immediate_percentage': [round(immediate_percent, 2)]})