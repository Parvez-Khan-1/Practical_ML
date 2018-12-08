
def mean(values):
    return sum(values)/len(values)


def variance(values, mean):
    return sum([(x - mean) ** 2 for x in values])


def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar