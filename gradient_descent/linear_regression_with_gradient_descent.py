import pandas as pd
import matplotlib.pyplot as plt
from packaging import markers

learning_rate = 0.01
iteration = 25

def read_csv():
    return pd.read_csv('data.csv')


def linear_regression(X_list, Y_list):
    a = 0.45
    b = 0.75
    Errors = []
    for i in range(iteration):
        SSE = 0
        gradient_a = 0
        gradient_b = 0
        for idx, X in enumerate(X_list):
            Yp = a + (b*X)
            SSE += squared_error(Y_list[idx], Yp)
            gradient_a += gradient_of_a(Y_list[idx], Yp)
            gradient_b += gradient_of_b(Y_list[idx], Yp, X)
        Errors.append(SSE)
        print("SQUARED ERROR : ", SSE)
        a = update_coefficients(a, gradient_a)
        b = update_coefficients(b, gradient_b)
    return Errors

def update_coefficients(a, gradient):
    return (a - learning_rate * gradient)


def gradient_of_a(Y, Yp):
    return -(Y-Yp)


def gradient_of_b(Y, Yp, X):
    return -(Y-Yp)*X


def normalization(val_list):
    normalized = []
    min_val = min(val_list)
    max_val = max(val_list)
    for val in val_list:
        normalized.append((val-min_val)/(max_val-min_val))
    return normalized


def squared_error(Y, Yp):
    return 0.5*((Y-Yp)**2)


def visualize(Y):
    X = list(range(1, iteration+1))
    plt.plot(X, Y, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Squared Error')
    plt.show()



if __name__ == '__main__':
    data_frame = read_csv()
    X_list = list(data_frame['Size'])
    Y_list = list(data_frame['Price'])

    X_list = normalization(X_list)
    Y_list = normalization(Y_list)

    Errors = linear_regression(X_list, Y_list)
    visualize(Errors)
