from keras import Sequential
from keras.callbacks import ModelCheckpoint, History, EarlyStopping
from keras.layers import Dense, Dropout
from matplotlib import pyplot
import sys
from normalize import X_scaled, y
from utility import split_data

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

# Accuracy: 0.77
