import pandas as pd
from matplotlib import pyplot as plt

LEARNING_RATE = 0.01


def load_data_set(file_path):
    return pd.read_csv(file_path)


def linear_regression(intercept, slope, input_val):
    return intercept + slope * input_val


def get_coefficient(X, Y, epochs):
    intercept = 0.0
    slope = 0.0

    for epoch in range(epochs):
        for xi, yi in zip(X, Y):
            input_error = linear_regression(intercept, slope, xi)

            # error input_error - output
            error = input_error - yi
            intercept = calculate_intercept(intercept, error)
            slope = calculate_slope(slope, error, xi)

    return intercept, slope


def calculate_intercept(intercept, error):
    updated_intercept = intercept - LEARNING_RATE * error
    return updated_intercept


def calculate_slope(slope, error, input_val):
    updated_slope = slope - LEARNING_RATE * error * input_val
    return updated_slope


def make_predictions(X, Y, intercept, slope):
    return [linear_regression(intercept, slope, xi) for xi, yi in zip(X, Y)]


def show_graph(X, Y, predicted_values=None):
    plt.scatter(X, Y)
    if predicted_values is not None:
        plt.plot(X, predicted_values)
    plt.xlabel("Height Of a Person")
    plt.ylabel("Weight Of a Person")
    plt.title("Making a Simple_Linear_Regression Line")
    plt.show()


if __name__ == '__main__':
    data_set = load_data_set('data.csv')

    X = data_set['X']
    Y = data_set['Y']

    show_graph(data_set['X'], data_set['Y'])
    intercept, slope = get_coefficient(X, Y, epochs=2)
    predicted_values = make_predictions(X, Y, intercept, slope)
    show_graph(X, Y, predicted_values)