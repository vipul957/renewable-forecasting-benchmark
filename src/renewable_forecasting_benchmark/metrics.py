"""Forecasting metrics with explicit zero-denominator behavior."""
from __future__ import annotations
import numpy as np

def mae(actual, predicted) -> float: return float(np.mean(np.abs(np.asarray(actual)-np.asarray(predicted))))
def rmse(actual, predicted) -> float: return float(np.sqrt(np.mean((np.asarray(actual)-np.asarray(predicted))**2)))
def smape(actual, predicted) -> float:
    a, p = np.asarray(actual, float), np.asarray(predicted, float)
    denom = np.abs(a) + np.abs(p)
    return float(np.mean(np.divide(2*np.abs(a-p), denom, out=np.zeros_like(denom), where=denom != 0)))
