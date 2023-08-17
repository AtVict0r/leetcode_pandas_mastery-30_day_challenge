import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_employee = employee.sort_values(by='salary', ascending=False)
    unique_salaries = sorted_employee['salary'].unique()
    try:
        second_highest = unique_salaries[1]
    except IndexError:
        # If no second highest salary exists
        second_highest = None
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})