from sklearn import datasets
from sklearn.linear_model import LogisticRegression

X, y = datasets.load_iris(return_X_y=True)

X_DATA = [[25, 55, 20000],
          [20, 45, 0],
          [27, 59, 21000],
          [23, 55, 10000],
          [29, 77, 0],
          [19, 50, 0]
          ]

Y_DATA = [[1], [1], [1], [0], [0], [0]]

classifier = LogisticRegression()

classifier.fit(X_DATA, Y_DATA)


TEST_DATA = [[15, 39, 0]]

predicted_result = classifier.predict(TEST_DATA)

print(predicted_result)
