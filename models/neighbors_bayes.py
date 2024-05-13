from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from normalize import X_scaled, y

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)

k_range = range(1, 26)
scores = {}
matrices = {}
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train.values.ravel())
    y_pred = knn.predict(X_test)
    scores[k] = knn.score(X_test, y_test)
    matrices[k] = confusion_matrix(y_test, y_pred)

print(scores)
print(matrices)

gnb = GaussianNB()
gnb.fit(X_train, y_train.values.ravel())
y_pred = gnb.predict(X_test)
score = gnb.score(X_test, y_test)
matrix = confusion_matrix(y_test, y_pred)

print(f'Naive Bayes accuracy: {score:.2f}')
print(f'Naive Bayes confusion matrix:\n{matrix}')


# 15KN accuracy: 0.7429
# 15KN confusion matrix:
# [[1134  317]
#  [ 329  732]]

# Naive Bayes accuracy: 0.71
# Naive Bayes confusion matrix:
# [[1075  411]
#  [ 310  716]]
