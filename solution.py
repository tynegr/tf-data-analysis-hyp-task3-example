import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import permutation_test

chat_id = 298754188 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    return stats.ttest_ind(x, y)[1] < 0.01 # Ваш ответ, True или False

# def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
#     # Измените код этой функции
#     # Это будет вашим решением
#     # Не меняйте название функции и её аргументы
    
#     alpha = 0.09
#     effect = permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), 
#                  vectorized=True, 
#                  n_resamples=5000,
#                  alternative='greater').pvalue < alpha
#     return effect # Ваш ответ, True или False
