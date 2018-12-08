import pandas as pd
import numpy as np
from math import sqrt
from Simple_Linear_Regression import SLRHelper
import matplotlib.pyplot as plt


def read_csv(file_path):
    return pd.read_csv(file_path)


def split_data_set(data_frame):
    msk = np.random.rand(len(data_frame)) < 0.8
    train = data_frame[msk]
    test = data_frame[~msk]
    return train, test


def coefficients(train):
    x, y = get_x_and_y(train)
    x_mean, y_mean = SLRHelper.mean(x), SLRHelper.mean(y)
    b1 = SLRHelper.covariance(x, x_mean, y, y_mean) / SLRHelper.variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]


def get_x_and_y(train):
    x = []
    y = []
    for row in train.iterrows():
        x.append(row[1]['Height'])
        y.append(row[1]['Weight'])
    return x, y


def simple_linear_regression(test, b0, b1):
    predicted = []
    actual = []
    for row in test.iterrows():
        independent_var = row[1]['Height']
        dependent_var = b0 + b1 * independent_var
        predicted.append(dependent_var)
        actual.append(row[1]['Weight'])
    return actual, predicted


# Calculate root mean squared error
def rmse_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)


def visualize_regression_line(train_x, train_y, intercept, slope):

    for x in train_x:
        print(x)
        print((slope*x) + intercept)
    # reg_line = [(slope*x)+intercept for x in train_x]
    #
    # plt.scatter(train_x, train_y, edgecolors="red")
    # plt.plot(train_x, reg_line)
    # plt.ylabel("Dependent Variable")
    # plt.xlabel("Independent Variable")
    # plt.title("Making a regression line")
    # plt.show()


if __name__ == '__main__':
    data_frame = read_csv('ht_wt_dataset.csv')
    train, test = split_data_set(data_frame)
    b0, b1 = coefficients(train)
    actual, predicted = simple_linear_regression(test, b0, b1)
    rmse_error = rmse_metric(actual, predicted)
    print("Root Mean Squared Error : %.3f"%rmse_error)