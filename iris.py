from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt


iris = load_iris()

knn = KNeighborsClassifier(n_neighbors=1)
logreg = LogisticRegression()

X = iris['data']
y = iris['target']

knn.fit(X,y)
logreg.fit(X,y)

x_new = [[0.3,2.2,4.6,1.2],[4.1,2.5,2.3,0.9]]

# prediction based on the models
print knn.predict(x_new)
print logreg.predict(x_new)

# checking the model accuracy
y_pred = logreg.predict(X)
y_pred2 = knn.predict(X)

# To check the correct input and output check length print len(y_pred)

print metrics.accuracy_score(y,y_pred)
print metrics.accuracy_score(y,y_pred2)

# split the two into train and test
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.4, random_state=2)

# Validating the lines spit
# print X_train.shape
# print y_test.shape

# Train the model
logreg.fit(X_train,y_train)
knn.fit(X_train,y_train)

# Test the model
y_pred3 = logreg.predict(X_test)
y_pred4 = knn.predict(X_test)

# Check the accuracy
print metrics.accuracy_score(y_test,y_pred3)
print metrics.accuracy_score(y_test,y_pred4)

# Check best value for K
k_range = range(1, 26)
score = []
for i in k_range:
    knn2 = KNeighborsClassifier(n_neighbors=i)
    knn2.fit(X_train,y_train)
    y_pred5 = knn2.predict(X_test)
    score.append(metrics.accuracy_score(y_test,y_pred5))

# check all the score in a graph
plt.plot(k_range,score)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')
plt.show()