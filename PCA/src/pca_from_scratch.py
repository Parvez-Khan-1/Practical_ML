from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig
# define a matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
print('---------------------------------')
# calculate the mean of each column
M = mean(A.T, axis=1)
print(M)
print('---------------------------------')
# center columns by subtracting column means
C = A - M
print(C)
print('---------------------------------')
# calculate covariance matrix of centered matrix
V = cov(C.T)
print(V)
print('---------------------------------')
# eigendecomposition of covariance matrix
values, vectors = eig(V)
print(vectors)
print('---------------------------------')
print(values)
print('---------------------------------')
# project data
P = vectors.T.dot(C.T)
print(P.T)
print('---------------------------------')