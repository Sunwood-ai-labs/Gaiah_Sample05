# plotting.py
# データの可視化を行う

import matplotlib.pyplot as plt

def plot_data(x, y):
    """データを散布図としてプロット"""
    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Data Plot')
    plt.show()