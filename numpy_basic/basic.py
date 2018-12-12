import numpy as np
import random

# create a simple 3x3 vector with random values
narray = np.arange(9).reshape(3, 3)

# find indices of non-zero elements in a vector
narray = [1, 0, 2, 3, 5, 0, 9, 3]
non_zero_idx = np.nonzero(narray)


# create a 3x3 identity matrix
matrix = np.eye(4, 4)

# Create a random vector of size 30 and find the mean value

# False Solution
Z = np.arange(30)
print(Z)
mean_val = Z.mean()
print(mean_val)


# True Solution
Z = np.random.random(30)
print(Z)
m = Z.mean()
print(m)