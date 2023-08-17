import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sort_scores = scores.sort_values(by='score', ascending=False)
    sort_scores['rank'] =  sort_scores['score'].rank(method='dense', ascending=False)
    return sort_scores[['score', 'rank']]