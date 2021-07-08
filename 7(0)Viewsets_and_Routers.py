# Serializer : 
# Serializers are responsible for converting objects into data types understandable by javascript and front-end frameworks.
# provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

# Viewsets 
# api_basic/views.py:
'''
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class TeacherViewSet(viewsets.ViewSet):
    def list(self,request):
        # Get all Teachers from database
        teachers = Teacher.objects.all()
        # need to Teacher serialize 
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = TeacherSerializer(data=request.data)

        # Check If our serializer is valid or not?
        if serializer.is_valid():
            # If our serializer is valid then we are going to save serializer
            serializer.save()
            # status=201 is created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        # Get all Teachers from database
        queryset = Teacher.objects.all()
        teacher = get_object_or_404(queryset,pk=pk)
        # need to Teacher serialize 
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def update(self,request,pk=None):
        teacher = Teacher.objects.get(pk=pk)
        # need to Teacher serializer and pass the data
        serializer = TeacherSerializer(teacher,data=request.data)
        # Check If our serializer is valid or not?
        if serializer.is_valid():
            # If our serializer is valid then we are going to save serializer
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

# api_basic/urls.py:
'''
from django import urls
from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import GenericAPIView, TeacherViewSet, Teacher_list, teacher_detail, TeacherAPIView, TeacherDetails
from rest_framework.routers import DefaultRouter                        *****

router = DefaultRouter()                                                *****
router.register('teacher',TeacherViewSet,basename='teacher')            *****

urlpatterns = [
    path('viewset/',include(router.urls)),              *****
    path('viewset/<int:pk>/',include(router.urls)),     *****

    # path('teacher/', Teacher_list), 
    path('teacher/', TeacherAPIView.as_view()),
    # path('detail/<int:pk>',teacher_detail),
    path('detail/<int:id>',TeacherDetails.as_view()),
    path('generic/teacher/',GenericAPIView.as_view()),
]
'''

# Run the server:
'''python manage.py runserver'''

# Copy the link:
'''localhost:8000/viewset/teacher'''

# OUTPUT : 
'''
Api Root / Teacher List

Teacher List

GET /viewset/teacher/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "Firstname": "Disha",
        "Lastname": "Vekariya",
        "Email": "vd@gmail.com",
        "DOB": "2021-06-15"
    },
    {
        "Firstname": "Jigs",
        "Lastname": "Patel",
        "Email": "jp@gmail.com",
        "DOB": "2021-06-16"
    },
    {
        "Firstname": "Rahul",
        "Lastname": "Makwana",
        "Email": "mr@gmail.com",
        "DOB": "2021-06-16"
    },
    {
        "Firstname": "Ankita",
        "Lastname": "Makwana",
        "Email": "am@gmail.com",
        "DOB": "2021-06-16"
    },
    {
        "Firstname": "Rahul",
        "Lastname": "Makwana",
        "Email": "mr@gmail.com",
        "DOB": "2021-06-16"
    }
]
'''

# You can also add the data below content section and POST the data.

# You can also update the data below section and PUT the data (For def update)
# copy this link:

'''localhost:8000/viewset/teacher/2 or 4 or 5 or 6 or 7'''              