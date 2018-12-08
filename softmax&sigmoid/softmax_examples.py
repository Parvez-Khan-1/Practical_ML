# Required Python Packages
import numpy as np
import math


def calculate_softmax_without_numpy(scores):
    z_exp = [math.exp(i) for i in scores]
    sum_z_exp = sum(z_exp)
    softmax = [i / sum_z_exp for i in z_exp]
    return softmax


def calculate_softmax_using_numpy(scores):
    """
    Calculate the softmax for the given scores
    :param scores:
    :return:
    """
    return np.exp(scores) / np.sum(np.exp(scores), axis=0)


if __name__ == "__main__":
    logits = [8, 5, 2]
    logits = [1, 2, 3, 4, 1, 2, 3]
    print("Softmax :: ", calculate_softmax_without_numpy(logits))