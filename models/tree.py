from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from normalize import X_scaled, y

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

train_pred = dtc.predict(X_train)
test_pred = dtc.predict(X_test)

train_acc = dtc.score(X_train, y_train)
test_acc = dtc.score(X_test, y_test)

print(f'Training accuracy: {train_acc:.2f}')
print(f'Test accuracy: {test_acc:.2f}')

cm_train = confusion_matrix(y_train, train_pred)
cm_test = confusion_matrix(y_test, test_pred)

print(f'Training confusion matrix:\n{cm_train}')
print(f'Test confusion matrix:\n{cm_test}')

# Training accuracy: 0.99
# Test accuracy: 0.70
# Training confusion matrix:
# [[3376    7]
#  [  39 2438]]
# Test confusion matrix:
# [[1086  385]
#  [ 365  676]]
