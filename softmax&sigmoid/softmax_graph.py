import numpy as np
import matplotlib.pyplot as plt


def softmax(inputs):
    """
    Calculate the softmax for the give inputs (array)
    :param inputs:
    :return:
    """
    return np.exp(inputs) / float(sum(np.exp(inputs)))


def line_graph(x, y, x_title, y_title):
    """
    Draw line graph with x and y values
    :param x:
    :param y:
    :param x_title:
    :param y_title:
    :return:
    """
    plt.plot(x, y)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()


X = [1, 2, 3, 4, 5]
softmax_scores = softmax(X)
print(softmax_scores)

line_graph(X, softmax_scores, "Inputs", "Softmax Scores")