# api_basic/views.py:
'''
from rest_framework.authentication import SessionAuthentication, BasicAuthentication            *****
from rest_framework.permissions import IsAuthenticated

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
                    serializer_class = TeacherSerializer
                    queryset = Teacher.objects.all()
                    lookup_field = 'id'
                    authentication_classes = [SessionAuthentication, BasicAuthentication]       *****
                    permission_classes = [IsAuthenticated]

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

# Run the server:
'''python manage.py runserver'''
# Copy this link:
'''http://localhost:8000/generic/teacher/'''

# OUTPUT:
'''
HTTP 403 Forbidden
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "Authentication credentials were not provided."
}
'''


# After 6Tokens.py Process:
# If you are add TokenAuthentication then:
# api_basic/views.py:
'''
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authentication import TokenAuthentication           *****
from rest_framework.permissions import IsAuthenticated

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
                    serializer_class = TeacherSerializer
                    queryset = Teacher.objects.all()
                    lookup_field = 'id'
                    # authentication_classes = [SessionAuthentication, BasicAuthentication]
                    authentication_classes = [TokenAuthentication]              *****
                    permission_classes = [IsAuthenticated]

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

# OUTPUT:
'''
HTTP 401 Unauthorized
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
WWW-Authenticate: Token                                                 *****

{
    "detail": "Authentication credentials were not provided."
}
'''