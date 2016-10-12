from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression



iris = load_iris()
knn = KNeighborsClassifier()
logreg = LogisticRegression()
X = iris['data']
y = iris['target']
knn.fit(X,y)
logreg.fit(X,y)
x_new = [[3,2,1,2]]

print knn.predict(x_new)