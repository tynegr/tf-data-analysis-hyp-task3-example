import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 462449141 # Ваш chat ID, не меняйте название переменной

SGN_LVL = 0.01

def solution(x: np.array, y: np.array) -> bool:
    pval = mannwhitneyu(x, y, alternative="less").pvalue
    if pval < SGN_LVL:
        return True
    # true: выборки не равны
    return False
