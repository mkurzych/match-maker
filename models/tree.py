from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from models.utility import split_data
from normalize import X_scaled, y


def train_model(X_train, y_train):
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    return dtc


def evaluate_model(model, X, y):
    pred = model.predict(X)
    acc = model.score(X, y)
    cm = confusion_matrix(y, pred)
    return acc, cm


def print_metrics(name, acc, cm):
    print(f'{name} accuracy: {acc:.2f}')
    print(f'{name} confusion matrix:\n{cm}')


# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = split_data(X_scaled, y)

# Train the model
dtc = train_model(X_train, y_train)

# Evaluate the model
train_acc, cm_train = evaluate_model(dtc, X_train, y_train)
test_acc, cm_test = evaluate_model(dtc, X_test, y_test)

# Print the metrics
print_metrics('Training', train_acc, cm_train)
print_metrics('Test', test_acc, cm_test)

# Training accuracy: 0.99
# Test accuracy: 0.70
# Training confusion matrix:
# [[3376 7]
# [ 39 2438]]
# Test confusion matrix:
# [[1086 385]
# [ 365 676]]
