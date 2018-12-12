import numpy as np

# create a random matrix 5x5
matrix = np.random.random((5, 5))
print(matrix)
print("-"*25)

max, min = matrix.max(), matrix.min()
normalize_matrix = (matrix - min) / (max - min)
print(normalize_matrix)