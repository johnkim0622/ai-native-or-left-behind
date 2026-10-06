"""
helpers.py: reusable functions
import in notebooks with : from src.helpers import weighted_pct
"""


def weighted_pct(data, col, weight="weight"):
    """ Weighted percentage of 1s in a 0/1 col
    data" DataFrame
    col: name of a 0/1 column
    weight: name of weight column
    returns a percentage, rows where col is dropped
    """

    d = data[[col, weight]].dropna()
    return 100 * (d[col] * d[weight]).sum() / d[weight].sum()