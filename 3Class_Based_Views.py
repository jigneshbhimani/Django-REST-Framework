# Class Based API Views (['GET','POST'])
# api_basic/views.py
'''
from rest_framework.views import APIView

class TeacherAPIView(APIView):

    # GET Method:
    def get(self,request):
        # Get all Teachers from database
            teachers = Teacher.objects.all()
            # need to Teacher serialize 
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)

    # POST Method:
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        # Check If our serializer is valid or not?
        if serializer.is_valid():
            # If our serializer is valid then we are going to save serializer
            serializer.save()
            # status=201 is created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

# api_basic/urls.py:
'''
from django.urls import path
from .views import Teacher_list, teacher_detail, TeacherAPIView

urlpatterns = [
    # path('teacher/', Teacher_list),
    path('teacher/', TeacherAPIView.as_view()),
    path('detail/<int:pk>',teacher_detail),
]
'''

# Run the server
'''python manage.py runserver'''

# OUTPUT:
'''
Teacher Api

GET /teacher/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "Firstname": "Jignesh",
        "Lastname": "Patel",
        "Email": "jp@gmail.com",
        "DOB": "2021-06-15"
    },
    {
        "Firstname": "Disha",
        "Lastname": "Vekariya",
        "Email": "vd@gmail.com",
        "DOB": "2021-06-15"
    }
]
'''

# If you need to create:
# Go to The localhost:8000/teacher and below content section
# Example:
'''
{
        "Firstname": "Jignesh",                             # I need to change Jigs from Jignesh
        "Lastname": "Patel",
        "Email": "jp@gmail.com",
        "DOB": "2021-06-15"
    }
'''

# Then click the POST button. and show the OUTPUT:
'''
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "Firstname": "Jigs",
    "Lastname": "Patel",
    "Email": "jp@gmail.com",
    "DOB": "2021-06-16"
}
'''

# If you want to GET back data then click the right side upper GET button and OUTPUT is:
'''
HTTP 200 OK
Allow: GET, OPTIONS, POST, HEAD
Content-Type: application/json
Vary: Accept

[
    {
        "Firstname": "Jignesh",
        "Lastname": "Patel",
        "Email": "jp@gmail.com",
        "DOB": "2021-06-15"
    },
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
        "DOB": "2021-06-15"
    }
]
'''





# Class Based API Views (['GET','PUT','DELETE'])
# api_basic/views.py
'''
class TeacherDetails(APIView):

    def get_object(self, id):
        try:
            return Teacher.objects.get(id=id)
        except Teacher.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # GET Method:
    def get(self,request,id):
        teacher = self.get_object(id)
        # need to Teacher serializer
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    # PUT Method:
    def put(self,request,id):
        teacher = self.get_object(id)
        # need to Teacher serializer and pass the data
        serializer = TeacherSerializer(teacher,data=request.data)
        # Check If our serializer is valid or not?
        if serializer.is_valid():
            # If our serializer is valid then we are going to save serializer
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE Method:
    def delete(self,request,id):
        teacher = self.get_object(id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

# api_basic/urls.py:
'''
from django.urls import path
from .views import Teacher_list, teacher_detail, TeacherAPIView, TeacherDetails

urlpatterns = [
    # path('teacher/', Teacher_list),
    path('teacher/', TeacherAPIView.as_view()),
    # path('detail/<int:pk>',teacher_detail),
    path('detail/<int:id>',TeacherDetails.as_view()),
]
'''

# Run the Server:
'''python manage.py runserver'''
# Copy the link:
'''localhost:8000/detail/1'''
# OUTPUT 1:
'''
HTTP 200 OK
Allow: PUT, OPTIONS, GET, DELETE, HEAD
Content-Type: application/json
Vary: Accept

{
    "Firstname": "Jignesh",
    "Lastname": "Patel",
    "Email": "jp@gmail.com",
    "DOB": "2021-06-15"
}
'''

# Copy the link:
'''localhost:8000/detail/2'''
# OUTPUT 2:
'''
HTTP 200 OK
Allow: DELETE, PUT, OPTIONS, GET, HEAD
Content-Type: application/json
Vary: Accept

{
    "Firstname": "Disha",
    "Lastname": "Vekariya",
    "Email": "vd@gmail.com",
    "DOB": "2021-06-15"
}
'''


# If you need to change some field data
# Go to The localhost:8000/deatil/1 or /2 and below content section
# Example:
'''
{   
    "Firstname": "Rahul",                       # Change Rahul from Jignesh
    "Lastname": "Patel",
    "Email": "jp@gmail.com",
    "DOB": "2021-06-15"
}
'''

# Then click the PUT button. and show the OUTPUT:
'''
HTTP 200 OK
Allow: DELETE, PUT, OPTIONS, GET, HEAD
Content-Type: application/json
Vary: Accept

{
    "Firstname": "Rahul",
    "Lastname": "Patel",
    "Email": "jp@gmail.com",
    "DOB": "2021-06-15"
}
'''

# If you want to delete some data
# Go to The localhost:8000/deatil/1 or /2 and click the right side upper DELETE button
# OUTPUT:
'''
DELETE /detail/1

HTTP 204 No Content
Allow: PUT, OPTIONS, DELETE, GET, HEAD
Content-Type: application/json
Vary: Accept
'''


