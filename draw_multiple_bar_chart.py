# Sampath Thennakoon
# 16/04/2023

import numpy as np
import matplotlib.pyplot as plt

def draw_chart():
    X = ["WALK", "IMMOB.", "MEET", "BROWSE", "FIGHT", "DROPDOWN", "LEAVE"]
    Ytrain = [1200, 326, 628, 741, 180, 430, 26]
    Ytest = [619, 168, 326, 338, 116, 210, 8]
    Yvalidation = [171, 71, 105, 140, 29, 68, 3]

    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.1, Ytrain, 0.1, label='Train')
    plt.bar(X_axis, Ytest, 0.1, label='Test')
    plt.bar(X_axis + 0.1, Yvalidation, 0.1, label='Validation')

    plt.xticks(X_axis, X)
    plt.xlabel("CAVIAR Action Classes")
    plt.ylabel("Number of Occurrences")
    plt.title("CAVIAR Action Class Distribution Over The Train, Test And Validation Data Set")
    plt.legend()

    plt.savefig('1.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    draw_chart()
