# matrix_operations.py
# NumPyを使用した行列操作

import numpy as np

def create_matrix(rows, cols):
    """指定されたサイズの行列を生成"""
    return np.random.rand(rows, cols)

def multiply_matrices(A, B):
    """二つの行列を乗算"""
    return np.dot(A, B)