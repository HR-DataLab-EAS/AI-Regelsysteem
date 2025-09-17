#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def analyse_mnist(data, labels, naam):
    print(f"\n--- {naam} ---")
    print("Shape:", data.shape)
    print("Label shape:", labels.shape)
    print("Unieke labels:", np.unique(labels))
    print("Pixelwaarde bereik:", np.min(data), "-", np.max(data))
    print("Voorbeeldlabel:", labels[0])
    print("Voorbeeldafbeelding:\n", data[0])

# Data laden
mnist = tf.keras.datasets.mnist
(training_data, training_labels), (test_data, test_labels) = mnist.load_data()

# Analyse voor normalisatie
analyse_mnist(training_data, training_labels, "Trainingset (origineel)")
analyse_mnist(test_data, test_labels, "Testset (origineel)")

# Normaliseren
training_data, test_data = training_data / 255.0, test_data / 255.0

# Analyse na normalisatie
analyse_mnist(training_data, training_labels, "Trainingset (genormaliseerd)")
analyse_mnist(test_data, test_labels, "Testset (genormaliseerd)")

# Model bouwen
model = tf.keras.Sequential([
    tf.keras.Input(shape=(28, 28)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Trainen
model.fit(training_data, training_labels, epochs=5)

# Evalueren
model.evaluate(test_data, test_labels)

# Voorspellingen
predictions = model.predict(test_data)
np.set_printoptions(suppress=True)
print("Voorbeeld testlabel:", test_labels[1])
print("Voorspelling:", predictions[1])

# Plot voorbeelden
def plot_examples(test_data, test_labels, predictions, num_examples=10):
    plt.figure(figsize=(12, 5))
    for i in range(num_examples):
        plt.subplot(2, 5, i + 1)
        plt.imshow(test_data[i], cmap='gray')
        plt.title(f"True: {test_labels[i]}\nPred: {np.argmax(predictions[i])}")
        plt.axis('off')
    plt.tight_layout()
    plt.show()

plot_examples(test_data, test_labels, predictions)
