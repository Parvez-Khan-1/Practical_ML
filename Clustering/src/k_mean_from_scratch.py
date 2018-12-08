from matplotlib import pyplot as plt
from copy import deepcopy
import pandas as pd
import numpy as np



data = pd.read_csv('../data/xclara.csv')

f1 = data['V1'].values
f2 = data['V2'].values

X = np.array(list(zip(f1, f2)))

plt.scatter(f1, f2, c='black', s=5)
plt.show()


# Euclidian Distance Calculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

# Number of clusters
k = 3

# X coordinates of random centroid
X_c = np.random.randint(0, np.max(X)-20, size=k)

# Y-Coordinated of randome centroid
Y_c = np.random.randint(0, np.max(X)-20, size=k)

C = np.array(list(zip(X_c, Y_c)), dtype=np.float32)

plt.scatter(f1, f2, c='#050505', s=7)
plt.scatter(X_c, Y_c, marker='*', s=200, c='g')

C_old = np.zeros(C.shape)

clusters = np.zeros(len(X))

error = dist(C, C_old, None)

while error!=0:

    for i in range(len(X)):
        distances = dist(X[i], C)
        cluster = np.argmin(distances)
        clusters[i] = cluster

    C_old = deepcopy(C)

    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
    error = dist(C, C_old, None)

colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='#050505')

plt.show()

print(C)

