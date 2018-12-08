# Singular-value decomposition
from numpy import array
from scipy.linalg import svd
# define a matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# SVD
U, s, V = svd(A)
print('-'*20)
print(U)
print('-'*20)
print(s)
print('-'*20)
print(V)


# Where A is the real m × n matrix that we wish to decompose,
# U is an m × m matrix,
# Σ (sigma) is an m × n diagonal matrix, and V
# T is the transpose of an n × n matrix