from rest_framework import viewsets, status
from rest_framework.response import Response
from app.models import Task
from app.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be created.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            validatedData = serializer.validated_data
            taskInstance = Task.objects.create(**validatedData)
            # Scrape movies
            
            return Response(TaskSerializer(taskInstance).data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
