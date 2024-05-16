import pandas as pd
from keras import Sequential
from keras.callbacks import ModelCheckpoint, History, EarlyStopping
from keras.layers import Dense, Dropout
from matplotlib import pyplot
import numpy as np
from sklearn.metrics import confusion_matrix
import sys
from normalize import X_scaled, y
from utility import split_data
import seaborn as sns

# Define constants
INPUT_SHAPE = 128
HIDDEN_LAYER_ONE = 64
HIDDEN_LAYER_TWO = 32
EPOCHS = 60
BATCH_SIZE = 32
DROPOUT_RATE = 0.5


def create_compile_model(input_shape, hidden_layer_one, hidden_layer_two, output_shape):
    model = Sequential([
        Dense(input_shape, activation='relu', input_shape=(input_shape,)),
        Dropout(DROPOUT_RATE),
        Dense(hidden_layer_one, activation='relu'),
        Dropout(DROPOUT_RATE),
        Dense(hidden_layer_two, activation='relu'),
        Dropout(DROPOUT_RATE),
        Dense(output_shape, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


def plot_metrics(history, metric, subplot, color_train='blue', color_test='orange'):
    pyplot.subplot(subplot)
    pyplot.title(metric)
    pyplot.plot(history.history[metric], color=color_train, label='train')
    pyplot.plot(history.history['val_' + metric], color=color_test, label='test')


def plot_confusion_matrix(y_true, y_pred):
    labels = np.array([0, 1])
    matrix = confusion_matrix(y_true, y_pred, labels=labels)
    ax = sns.heatmap(matrix, xticklabels='PN', yticklabels='PN', fmt='d', annot=True, square=True, cmap='Blues')
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    pyplot.tick_params(top=False, bottom=False, left=False, right=False)
    pyplot.yticks(rotation=0)
    filename = sys.argv[0].split('/')[-1]
    pyplot.savefig(filename + '_matrix.png')
    pyplot.show()


def summarize_diagnostics(history):
    plot_metrics(history, 'loss', 211)
    plot_metrics(history, 'accuracy', 212)
    filename = sys.argv[0].split('/')[-1]
    pyplot.savefig(filename + '_plot.png')
    pyplot.close()


# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = split_data(X_scaled, y)

# Create and compile the model
model = create_compile_model(X_train.shape[1], HIDDEN_LAYER_ONE, HIDDEN_LAYER_TWO, y.shape[1])

# Train the model
history = History()
checkpoint = ModelCheckpoint('model.keras', monitor='val_accuracy', save_best_only=True)
early_stopping = EarlyStopping(monitor='val_loss', patience=5)
model.fit(X_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_split=0.2, callbacks=[history, checkpoint, early_stopping])

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')

# Plot diagnostic learning curves
summarize_diagnostics(history)

# Make predictions
y_pred = model.predict(X_test)
y_pred = np.where(y_pred >= 0.5, 1, 0)
y_true = np.where(y_test >= 0.5, 1, 0)

# Plot confusion matrix
plot_confusion_matrix(y_true, y_pred)

# Accuracy: 0.76
