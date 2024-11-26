import cv2
from predict_image import Predict_cifar10

model_path = r"D:\code\CIFAR 10\cifar.keras"
weight_path = r"D:\code\CIFAR 10\cifar.weights.h5"
image_path = r"D:\code\CIFAR 10\ship man.jpg"
predict_man = Predict_cifar10(model_path, weight_path)

predicted_value = predict_man.predict(image_path)

image = cv2.imread(image_path)

cv2.putText(image, predicted_value, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()