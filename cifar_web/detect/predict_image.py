import cv2
import numpy as np
import tensorflow as tf


class Predict_cifar10:
    def __init__(self, model_path, weights_path):
        self.model = tf.keras.models.load_model(model_path)
        self.model.load_weights(weights_path)
        self.class_labels = [
            "Airplane",
            "Automobile",
            "Bird",
            "Cat",
            "Deer",
            "Dog",
            "Frog",
            "Horse",
            "Ship",
            "Truck",
        ]

    def preprocess_image(self, image):
        image = cv2.imread(image)
        image = cv2.resize(image, (32, 32))
        image = image / 255.0
        image = np.expand_dims(image, axis=0)
        return image

    def preprocess_frame(self, frame):
        frame = cv2.resize(frame, (32, 32))
        frame = frame / 255.0
        frame = np.expand_dims(frame, axis=0)
        return frame


    def predict(self, image):
        image = self.preprocess_image(image)
        prediction = self.model.predict(image)
        predicted_class = np.argmax(prediction, axis=1)
        return self.class_labels[predicted_class[0]]

    def predict_frame(self, frame):
        frame = self.preprocess_frame(frame)
        prediction = self.model.predict(frame)
        predicted_class = np.argmax(prediction, axis=1)
        return self.class_labels[predicted_class[0]]

