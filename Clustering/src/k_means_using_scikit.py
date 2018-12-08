from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


data = pd.read_csv('../data/xclara.csv')

f1 = data['V1'].values
f2 = data['V2'].values

X = np.array(list(zip(f1, f2)))


kmeans = KMeans(n_clusters=3)

kmeans = kmeans.fit(X)


labels = kmeans.predict(X)

centroids = kmeans.cluster_centers_

print(centroids)
