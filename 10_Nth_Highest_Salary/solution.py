import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_employee = employee['salary'].drop_duplicates().sort_values(ascending=False)

    try:
        return pd.DataFrame({'Nth Highest Salary': sorted_employee.iloc[[N-1]]})
    except IndexError:
        return pd.DataFrame({'Nth Highest Salary': [None]})