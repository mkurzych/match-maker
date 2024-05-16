from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from models.utility import split_data
from normalize import X_scaled, y


def train_evaluate_knn(X_train, y_train, X_test, y_test, k_range):
    scores = {}
    matrices = {}
    best_knn = None
    best_score = 0
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train.values.ravel())
        y_pred = knn.predict(X_test)
        score = knn.score(X_test, y_test)
        scores[k] = score
        matrices[k] = confusion_matrix(y_test, y_pred)
        if score > best_score:
            best_score = score
            best_knn = knn
    return scores, matrices, best_knn


def train_evaluate_gnb(X_train, y_train, X_test, y_test):
    gnb = GaussianNB()
    gnb.fit(X_train, y_train.values.ravel())
    y_pred = gnb.predict(X_test)
    score = gnb.score(X_test, y_test)
    matrix = confusion_matrix(y_test, y_pred)
    return score, matrix, gnb


def print_metrics(name, scores, matrices):
    print(f'{name} scores: {scores}')
    print(f'{name} confusion matrices:\n{matrices}')


# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = split_data(X_scaled, y)

# Train and evaluate the K-Nearest Neighbors model
k_range = range(1, 26)
knn_scores, knn_matrices, best_knn = train_evaluate_knn(X_train, y_train, X_test, y_test, k_range)

# Train and evaluate the Naive Bayes model
gnb_score, gnb_matrix, gnb = train_evaluate_gnb(X_train, y_train, X_test, y_test)

# Print the metrics
print_metrics('K-Nearest Neighbors', knn_scores, knn_matrices)
print_metrics('Naive Bayes', {' ': gnb_score}, {' ': gnb_matrix})

# 15KN accuracy: 0.7429
# 15KN confusion matrix:
# [[1134  317]
#  [ 329  732]]

# Naive Bayes accuracy: 0.71
# Naive Bayes confusion matrix:
# [[1075  411]
#  [ 310  716]]
