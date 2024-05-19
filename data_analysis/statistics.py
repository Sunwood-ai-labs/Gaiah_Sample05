# statistics.py
# データの統計情報を計算

import numpy as np

def calculate_mean(data):
    """データの平均を計算"""
    return np.mean(data)

def calculate_stddev(data):
    """データの標準偏差を計算"""
    return np.std(data)