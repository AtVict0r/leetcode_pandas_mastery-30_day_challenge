import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge orders and company tables
    merged_data = orders.merge(company, on='com_id', how='inner')
    
    # Filter rows with 'RED' company
    mask = merged_data['name'] == 'RED'
    sales_id = merged_data[mask]['sales_id'].unique()
    
    # Filter salespersons who don't have orders related to 'RED' company
    mask = ~sales_person['sales_id'].isin(sales_id)    
    return sales_person[mask][['name']]