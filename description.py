from predict_image import Predict_cifar10
import wikipediaapi as wiki

model_path = r"D:\code\CIFAR 10\cifar.keras"
weight_path = r"D:\code\CIFAR 10\cifar.weights.h5"
image_path = r"D:\code\CIFAR 10\plane man.jpg"

predict_man = Predict_cifar10(model_path, weight_path)

predicted_value = predict_man.predict(image_path)

print(f"The predicted value is {predicted_value}")

wiki_obj = wiki.Wikipedia("MyProjectName (merlin@example.com)", "en")
page = wiki_obj.page(str(predicted_value))
print(f"{page.summary.split('.')[0]}.{page.summary.split('.')[1]}")
