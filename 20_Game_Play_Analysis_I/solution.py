import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    return result.rename(columns={'event_date': 'first_login'})