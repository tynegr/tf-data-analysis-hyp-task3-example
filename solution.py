import pandas as pd
import numpy as np
from scipy.stats import permutation_test

chat_id = 462449141 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.01
    znach = permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), 
                 vectorized=True, 
                 n_resamples=5000,
                 alternative='greater').pvalue < alpha
    return znach # Ваш ответ, True или False
