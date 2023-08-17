import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    direct_report = employee.groupby('managerId').size().reset_index(name='count')
    mask = direct_report['count'] >= 5
    return employee.merge(direct_report[mask][['managerId']], how='inner', left_on='id', right_on='managerId')[['name']]