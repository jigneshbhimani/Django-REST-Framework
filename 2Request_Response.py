# 1.Request objects : 
# REST framework introduces a Request object that extends the regular HttpRequest, and provides more flexible request parsing.
# The core functionality of the Request object is the request.data attribute, which is similar to request.POST, but more useful for working with Web APIs.
'''
request.POST            # Only handles form data.  Only works for 'POST' method.
request.data            # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
'''


# 2.Response objects:
# REST framework also introduces a Response object, which is a type of TemplateResponse that takes unrendered content and uses content negotiation to determine the correct content type to return to the client.
'''
return Response(data)           # Renders to content type as requested by the client.
'''


# 3.Status codes:
# provides more explicit identifiers for each status code, such as HTTP_400_BAD_REQUEST in the status module.


# 4.Wrapping API views:
# REST framework provides two wrappers you can use to write API views.
# -> The @api_view decorator for working with function based views.
# -> The APIView class for working with class-based views.
# These wrappers provide a few bits of functionality such as making sure you receive Request instances in your view, and adding context to Response objects so that content negotiation can be performed.
# The wrappers also provide behaviour such as returning 405 Method Not Allowed responses when appropriate, and handling any ParseError exceptions that occur when accessing request.data with malformed input.


# 5.Pulling it all together:

# api_view() Decorator In Function Based API Views (['GET','POST'])
# api_basic/views.py:
''' add this:

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

...

@api_view(['GET','POST'])
def Teacher_list(request):

    # GET Method:
    # Get all Teachers from database
    if request.method == "GET":
        teachers = Teacher.objects.all()
        # need to Teacher serialize 
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    # POST Method:
    elif request.method == "POST":
        # need to Teacher serializer and pass the data
        serializer = TeacherSerializer(data=request.data)

        # Check If our serializer is valid or not?
        if serializer.is_valid():
            # If our serializer is valid then we are going to save serializer
            serializer.save()
            # status=201 is created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

# Run the server:
'''python manage.py runserver'''
# Copy the link:
'''localhost:8000/teacher'''
# OUTPUT:
'''
Teacher List

GET/teacher/

HTTP 200 OK
Allow: POST, GET, OPTIONS
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
        "Firstname": "Jigs",                             # I need to change Jigs from Jignesh
        "Lastname": "Patel",
        "Email": "jp@gmail.com",
        "DOB": "2021-06-15"
    }
'''
# Then click the POST button. and show the OUTPUT:
'''
HTTP 201 Created
Allow: GET, OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "Firstname": "Jigs",
    "Lastname": "Patel",
    "Email": "jp@gmail.com",
    "DOB": "2021-06-15"
}
'''

# If you want to GET back data then click the right side upper GET button and OUTPUT is:
'''
HTTP 200 OK
Allow: GET, OPTIONS, POST
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


# api_view() Decorator In Function Based API Views (['GET','PUT','DELETE'])
# api_basic/views.py:
'''
@api_view(['GET','PUT','DELETE'])
def teacher_detail(request,pk):
    # Retrieve, update or delete a code
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # GET Method:
    # Get all Teachers from database
    if request.method == "GET":
        # need to Teacher serializer
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    # PUT Method:
    elif request.method == "PUT":
        # need to Teacher serializer and pass the data
        serializer = TeacherSerializer(teacher,data=request.data)

        # Check If our serializer is valid or not?
        if serializer.is_valid():
            # If our serializer is valid then we are going to save serializer
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE Method:
    elif request.method == "DELETE":
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

# Run the Server:
'''python manage.py runserver'''
# Copy the link:
'''localhost:8000/detail/1'''
# OUTPUT 1:
'''
HTTP 200 OK
Allow: PUT, OPTIONS, GET, DELETE
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
Allow: DELETE, PUT, OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "Firstname": "Disha",
    "Lastname": "Vekariya",
    "Email": "vd@gmail.com",
    "DOB": "2021-06-15"
}
'''

# Copy the link:
'''localhost:8000/detail/3'''
# OUTPUT 3:
'''
HTTP 200 OK
Allow: DELETE, PUT, OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "Firstname": "Jigs",
    "Lastname": "Patel",
    "Email": "jp@gmail.com",
    "DOB": "2021-06-15"
}
'''

# If you need to change some field data
# Go to The localhost:8000/deatil/1 or /2 or /3 and below content section
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
Allow: DELETE, PUT, OPTIONS, GET
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
# Go to The localhost:8000/deatil/1 or /2 or /3 and click the right side upper DELETE button
# OUTPUT:
'''
DELETE /detail/3

HTTP 204 No Content
Allow: PUT, OPTIONS, DELETE, GET
Content-Type: application/json
Vary: Accept
'''