import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r'\bDIAB1\w*'
    mask = patients['conditions'].str.contains(pattern)
    return patients[mask].reset_index(drop=True)