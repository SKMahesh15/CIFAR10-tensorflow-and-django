**Image Classifier with CIFAR-10 and Wikipedia API**
This is a web application built using Django and TensorFlow. 
Users can upload an image, and the AI model will classify it into one of the 10 CIFAR-10 categories. 
The application then retrieves a description of the classified category using the Wikipedia API.

**CIFAR 10 Categories**
The classifier can identify the following categories:
Airplane
Automobile
Bird
Cat
Deer
Dog
Frog
Horse
Ship
Truck

**Technologies Used**
Django: Backend framework for handling requests and rendering templates.
TensorFlow: For the CIFAR-10 model.
Wikipedia API: To fetch category descriptions.
HTML/CSS: Used for simple forms and static pages (no JavaScript).

Setup Instructions
1. Clone the Repository
`git clone https://github.com/your-username/your-repository.git`

2. Install Dependencies
Install the required Python packages:
`pip install -r requirements.txt`

3. Configure Django
Ensure the TensorFlow model is saved in the correct directory (model/ by default).
Set up the database:
`python manage.py makemigrations
python manage.py migrate`

4. Run the Application
Start the Django development server:
`python manage.py runserver`
Open your browser and visit: http://127.0.0.1:8000/

**Screenshots**

![Dog photo example]("C:\Users\SK Mahesh\Pictures\Screenshots\Screenshot 2024-11-26 131258.png")

