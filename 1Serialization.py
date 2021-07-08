# 1.Setting up a new environment
'''python -m venv myvenv'''

# 2.Activate environment
'''myvenv\Scripts\activate'''

# 3.Install Django
'''pip install django'''

# 4.Install Django Rest Framework
'''pip install djangorestframework'''

# 5.Create a new project
'''django-admin startproject MyProject'''

# 6.Go to 'MyProject' folder
'''cd MyProject'''

# 7.Migrate
'''python manage.py migrate'''

# 8.Create a new app
'''python manage.py startapp api_basic'''

# 9.Create a super user
'''python manage.py createsuperuser'''

# 10.Add new 'api_basic' app and the 'rest_framework' app to 'INSTALLED_APPS'
# MyProject/settings.py:
'''
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api_basic',
]
'''

# 11.Create a Model
# api_basic/models.py:
'''
from django.db import models

class Teacher(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Email = models.EmailField(max_length=40)
    DOB = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Firstname
'''

# 12.Apply makemigrations
'''python manage.py makemigrations'''

# 13.Apply migrate
'''python manage.py migrate'''

# 14.Run the server
'''python manage.py runserver'''

# 15.Open in Browser
'''127.0.0.1:8000/admin''' 

# 16.Log in Djngo administartion
'''
User: Django
Password: 123
'''

# 17.Create a Teacher Model in Django Administartion

# 18.Creating a Serializer class
# Create a file in the api_basic directory and named 'serializers.py' 
# api_basic/serializers.py:
'''
from rest_framework import serializers
from .models import Teacher

# serializer class defines the fields that get serialized/deserialized.
class TeacherSerializer(serializers.Serializer):
    Firstname = serializers.CharField(max_length=20)
    Lastname = serializers.CharField(max_length=20)
    Email = serializers.EmailField(max_length=40)
    DOB = serializers.DateField()

# Create and return a new 'Teacher' instance, given the validated data
    def create(self, validated_data):
        return Teacher.objects.create(validated_data)


# Update and return an existing 'Teacher' instance, given the validated data.
    def update(self, instance, validated_data):
        instance.Firstname = validated_data.get('Firstname',instance.Firstname)
        instance.Lastname = validated_data.get('Lastname',instance.Lastname)
        instance.Email = validated_data.get('Email',instance.Email)
        instance.DOB = validated_data.get('DOB',instance.DOB)
        instance.save()
        return instance
'''
# The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save().
# A serializer class is very similar to a Django Form class, and includes similar validation flags on the various fields, such as required, max_length and default.


# 19.Working with Serializers
# In cmd:
'''python manage.py shell'''
'''
from api_basic.models import Teacher
from api_basic.serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
'''

# Now add teacher:
# In cmd:
'''
a = Teacher(Firstname = 'Jignesh', Lastname = 'Patel', Email = 'jp@gmail.com')
a.save()
a = Teacher(Firstname = 'Disha', Lastname = 'Vekariya', Email = 'vd@gmail.com')
a.save()
'''

# Get a few teacher instances
# In cmd:
'''
serializer = TeacherSerializer(a)
serializer.data
'OUTPUT': {'Firstname': 'Disha', 'Lastname': 'Vekariya', 'Email': 'vd@gmail.com', 'DOB': '2021-06-15'}
'''

# Translated the model instance into Python native datatypes.
# To finalize the serialization process we render the data into json.
# In cmd:
'''
content = JSONRenderer().render(serializer.data)
content
'OUTPUT': b'{"Firstname":"Disha","Lastname":"Vekariya","Email":"vd@gmail.com","DOB":"2021-06-15"}'
'''

# serialize querysets instead of model instances.
# Add a many=True flag to the serializer arguments.
# In cmd:
'''
serializer = TeacherSerializer(Teacher.objects.all(), many=True)
serializer.data
'OUTPUT': [OrderedDict([('Firstname', 'Jignesh'), ('Lastname', 'Patel'), ('Email', 'jp@gmail.com'), ('DOB', '2021-06-15')]),
          OrderedDict([('Firstname', 'Disha'), ('Lastname', 'Vekariya'), ('Email', 'vd@gmail.com'), ('DOB', '2021-06-15')])]
'''

# 20.Using ModelSerializers
# api_basic/serializers.py:
'''
from django.db.models import fields
from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['Firstname','Lastname','Email','DOB']
'''

# In cmd:
'''serializer = TeacherSerializer()'''
'''print(repr(serializer))'''
'''
'OUTPUT':
TeacherSerializer():
    Firstname = CharField(max_length=20)
    Lastname = CharField(max_length=20)
    Email = EmailField(max_length=40)
    DOB = DateField()
'''


# 21.Function Based API Views
# api_basic/views.py:
'''
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Teacher
from .serializers import TeacherSerializer

# Create your views here.

def Teacher_list(request):

    # GET Method:
    # Get all Teachers from database
    if request.method == "GET":
        teachers = Teacher.objects.all()
        # need to Teacher serialize 
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # POST Method:
    elif request.method == "POST":
        # create data using JsonParser to parse the data
        data = JSONParser().parse(request)
        # need to Teacher serializer and pass the data
        serializer = TeacherSerializer(data=data)

        # Check If our serializer is valid or not?
        if serializer.is_valid():
            # If our serializer is valid then we are going to save serializer
            serializer.save()
            # status=201 is created status
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
'''

# 22.MyProject/urls.py
'''
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api_basic.urls')),
]
'''

# Create a file in the api_basic directory and named 'urls.py'
# api_basic/urls.py:
'''
from django.urls import path
from .views import Teacher_list

urlpatterns = [
    path('teacher/', Teacher_list),   
]
'''

# Run the server
'''python manage.py runserver'''
# Copy the link in browser
'''
http://127.0.0.1:8000/teacher
'OUTPUT': [{"Firstname": "Jignesh", "Lastname": "Patel", "Email": "jp@gmail.com", "DOB": "2021-06-15"},
          {"Firstname": "Disha", "Lastname": "Vekariya", "Email": "vd@gmail.com", "DOB": "2021-06-15"}]
'''

# 23.Writing regular Django views using our Serializer
# We want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as csrf_exempt.
# Retrieve, update or delete a code
# api_basic/views.py:
'''
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Teacher
from .serializers import TeacherSerializer

...

@csrf_exempt
def teacher_detail(request,pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return HttpResponse(status=404)

    # GET Method:
    # Get all Teachers from database
    if request.method == "GET":
        # need to Teacher serializer
        serializer = TeacherSerializer(teacher)
        return JsonResponse(serializer.data, safe=False)

    # PUT Method:
    elif request.method == "PUT":
        # create data using JsonParser to parse the data
        data = JSONParser().parse(request)
        # need to Teacher serializer and pass the data
        serializer = TeacherSerializer(teacher,data=data)

        # Check If our serializer is valid or not?
        if serializer.is_valid():
            # If our serializer is valid then we are going to save serializer
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    # DELETE Method:
    elif request.method == "DELETE":
        teacher.delete()
        return HttpResponse(status=204)
'''

# api_basic/urls.py:
'''
from django.urls import path
from .views import Teacher_list, teacher_detail

urlpatterns = [
    path('teacher/', Teacher_list),
    path('detail/<int:pk>',teacher_detail),
]
'''

# Run the server:
'''python manage.py runserver'''
# Copy the Link:
'''http://127.0.0.1:8000/detail/1'''
'''OUTPUT: {"Firstname": "Jignesh", "Lastname": "Patel", "Email": "jp@gmail.com", "DOB": "2021-06-15"}'''
'''http://127.0.0.1:8000/detail/2'''
'''OUTPUT: {"Firstname": "Disha", "Lastname": "Vekariya", "Email": "vd@gmail.com", "DOB": "2021-06-15"}'''