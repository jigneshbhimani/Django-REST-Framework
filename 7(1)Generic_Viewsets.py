# Generic Viewset

# api_basic/views.py:
'''
class TeacherViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

                    serializer_class = TeacherSerializer
                    queryset = Teacher.objects.all()
'''
# Copy the link:

'''localhost:8000/viewset/teacher or /2 or /4 or /5 or /6 or /7 '''

# You can also Create, Update, Delete, Retrieve the data.