from django.shortcuts import render, HttpResponse
import cv2 
from detect.forms import ImageUploadForm
from .models import Image
from .predict_image import Predict_cifar10
import wikipediaapi as wiki

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()

            model_path = r"D:\code\CIFAR 10\cifar.keras"
            weight_path = r"D:\code\CIFAR 10\cifar.weights.h5"
            file_path = r"D:\code\CIFAR 10\cifar_web\media\image\image.jpg"
            predict_man = Predict_cifar10(model_path, weight_path)
            predicted_value = predict_man.predict(file_path)

            wiki_obj = wiki.Wikipedia("MyProjectName (merlin@example.com)", "en")
            page = wiki_obj.page(str(predicted_value))
            summary = f"{page.summary.split('.')[0]}.{page.summary.split('.')[1]}"

            context = {'uploaded_image':uploaded_image, 
                       'predicted_value': predicted_value,
                       'summary': summary}

            return render(request, 'detect/home.html', context)


    return render(request, "detect/home.html" )
