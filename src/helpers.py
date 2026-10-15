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


def weighted_ci(data, col, weight="weight", z=1.96):
    """ Weighted % of 1s in a 0/1 column, with a 95% confidence interval 
    Weighting makes sample act smaller than its real size, so CI uses Kish's effective sample size instead of n:
        n_eff = (sum of weights)^2 / (sum of squared weights)
        SE = sqrt(p(1-p) / n_eff)
        CI = p +/- 1.96 * SE        
    """
    d = data[[col, weight]].dropna()
    w = d[weight]
    p = (d[col] * w).sum() / w.sum()
    n_eff = w.sum() ** 2 / (w ** 2).sum()
    se = (p * (1-p) / n_eff) ** 0.5
    return {
        "pct": 100 * p,
        "se": 100 * se,
        "ci_lo": 100 * (p-z * se),
        "ci_hi": 100 * (p + z * se),
        "n": len(d),
        "n_eff": n_eff,

    }