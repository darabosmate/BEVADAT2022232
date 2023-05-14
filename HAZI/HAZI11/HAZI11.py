import tensorflow as tf
import numpy as np

def cifar100_data():
  train_images, train_labels, test_images, test_labels = tf.keras.datasets.cifar100.load_data()
  train_images = train_images / 255.0
  test_images = test_images / 255.0
  return train_images, train_labels, test_images, test_labels

def cifar100_model():
  model = tf.keras.models.Sequential([
      # Convolutional layer with 32 filters, 3x3 kernel size, and ReLU activation
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(32, 32, 3)),
    # Max pooling layer with 2x2 pool size
    tf.keras.layers.MaxPooling2D((2,2)),
    # Flatten layer to convert the 2D feature maps into a 1D feature vector
    tf.keras.layers.Flatten(),
    # Fully connected layer with 64 units and ReLU activation
    tf.keras.layers.Dense(64, activation='relu'),
    # Output layer with 100 units and softmax activation for classification
    tf.keras.layers.Dense(100, activation='softmax')
  ])
  return model

def model_compile(model):
  model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
  return model


def model_fit(model, epochs, train_images, train_labels):
  model.fit(epochs=epochs, x=train_images, y=train_labels)
  return model

def model_evaluate(model, test_images, test_labels):
  loss, acc = model.evaluate(test_images, test_labels, verbose=0)
  return (loss, acc)
