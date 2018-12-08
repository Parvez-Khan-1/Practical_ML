import matplotlib.pyplot as plt
from math import sqrt


def get_mean(values):
    return sum(values)/len(values)


def get_slope(x, x_mean, y, y_mean):
    # Calculating Slope Here
    #Sum((x-x_mean)*(y-y_mean))
    numerator = 0
    for i in range(len(x)):
        numerator += (x[i] - x_mean) * (y[i] - y_mean)
    denominator = sum((x_val - x_mean)**2 for x_val in x)
    slope = numerator / denominator
    return slope


def get_intercept(x_mean, y_mean, slope):
    #y_mean - slope * x_mean
    intercept = y_mean - slope * x_mean
    return intercept


def get_coefficients(independent_vars, dependent_vars):
    x_mean, y_mean = get_mean(independent_vars),get_mean(dependent_vars)
    slope = get_slope(independent_vars, x_mean, dependent_vars, y_mean)
    intercept = get_intercept(x_mean, y_mean, slope)
    return slope, intercept


def get_prediction_for_test_data(hours_studied_test, slope , intercept):
    predicted_val = [(intercept + slope * x_val) for x_val in hours_studied_test]
    return predicted_val


def calculate_root_mean_squared_error(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)


def show_x_and_y(independent_var, dependent_var):
    plt.scatter(independent_var, dependent_var)
    plt.xlabel("No of hours studied")
    plt.ylabel("Marks Obtained")
    plt.show()


def draw_regression_line(slope, intercept, independent_var, dependent_var):
    reg_line = [(intercept + slope * val) for val in independent_var]
    plt.scatter(independent_var, dependent_var)
    plt.plot(independent_var, reg_line)
    plt.xlabel("No of hours studied")
    plt.ylabel("Marks Obtained")
    plt.title("Making a Simple_Linear_Regression Line")
    plt.show()


def draw_actual_and_predicted_vals(hours_studied, actual_marks_obtained, predicted_marks_obtained):
    plt.scatter(hours_studied, actual_marks_obtained)
    plt.scatter(hours_studied, predicted_marks_obtained)
    plt.plot(hours_studied, predicted_marks_obtained)
    plt.xlabel("No of hours studied")
    plt.ylabel("Marks Obtained")
    plt.title("Making a Simple_Linear_Regression Line")
    plt.show()


if __name__ == '__main__':

    # train
    hours_studied = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
    obtained_marks = [35.0, 40.0, 50.0, 55.0, 65.0, 68.0, 72.0, 76.0, 78.0, 80.0, 82.0]

    # test
    hours_studied_test = [1.2, 1.8 , 2.0, 2.6, 3.8]
    obtained_marks_test = [36.0, 45.0, 50.0, 56.5, 66.0]

    slope, intercept = get_coefficients(hours_studied, obtained_marks)

    predicted_marks_for_test = get_prediction_for_test_data(hours_studied_test, slope , intercept)
    draw_actual_and_predicted_vals(hours_studied_test, obtained_marks_test, predicted_marks_for_test)
    print(obtained_marks_test)
    print(predicted_marks_for_test)
    print(calculate_root_mean_squared_error(obtained_marks_test, predicted_marks_for_test))
