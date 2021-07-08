# You can create, update, retrieve and delete the data from the output.(In browser)

# api_basic/views.py:
'''
from rest_framework import generics
from rest_framework import mixins

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
                    
                    serializer_class = TeacherSerializer
                    queryset = Teacher.objects.all()
                    lookup_field = 'id'

                    def get(self,request,id=None):
                        if id:
                            return self.retrieve(request)
                        else:
                            return self.list(request)

                    def post(self,request):
                        return self.create(request)

                    def put(self,request,id=None):
                        return self.update(request,id)
                    
                    def delete(self,request,id):
                        return self.destroy(request,id)
'''

# api_basic/urls.py:
'''
from django.urls import path
from .views import GenericAPIView, Teacher_list, teacher_detail, TeacherAPIView, TeacherDetails

urlpatterns = [
    # path('teacher/', Teacher_list), 
    path('teacher/', TeacherAPIView.as_view()),
    # path('detail/<int:pk>',teacher_detail),
    path('detail/<int:id>',TeacherDetails.as_view()),
    path('generic/teacher/',GenericAPIView.as_view()),
]
'''

# Run the server:
'''python manage.py runserver'''

# Copy this link:
'''localhost:8000/generic/teacher'''

# OUTPUT:
'''
Generic Api

GET /generic/teacher/

HTTP 200 OK
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
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
    }
]
'''

# Now if you want to add some data in the output(browser)
# then, In the output page below Firstname, Lastname and Email column will be there.
'''
Firstname : Ankita
Lastname : Makwana
Email : am@gmail.com
'''
# You can add this field and click the button POST.
# After click the POST button:
'''
HTTP 201 Created
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "Firstname": "Ankita",
    "Lastname": "Makwana",
    "Email": "am@gmail.com",
    "DOB": "2021-06-16"
}
'''
# Now click the button GET:
'''
HTTP 200 OK
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
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
        "Firstname": "Ankita",
        "Lastname": "Makwana",
        "Email": "am@gmail.com",
        "DOB": "2021-06-16"
    }
]
'''
# You can also Delete, Retrieve the data.