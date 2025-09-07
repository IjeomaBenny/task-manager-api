from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
import django_filters.rest_framework as dj_filters

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, deleting,
    and marking tasks as complete. Includes filtering & sorting.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Filters & sorting
    filter_backends = [dj_filters.DjangoFilterBackend, filters.OrderingFilter]
    # ?status=Pending  |  ?priority=High  |  ?due_date__gte=2025-09-10
    filterset_fields = {
        'status': ['exact'],
        'priority': ['exact'],
        'due_date': ['exact', 'gte', 'lte'],
    }
    # ?ordering=due_date  |  ?ordering=-priority
    ordering_fields = ['due_date', 'priority']
    ordering = ['due_date']  # default ordering

    def get_queryset(self):
        # Only the logged-in user's tasks
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Attach owner automatically
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['patch'])
    def complete(self, request, pk=None):
        """
        PATCH /tasks/<id>/complete/
        Marks a task as Completed and sets completed_at.
        """
        task = self.get_object()
        task.status = 'Completed'
        task.completed_at = timezone.now()
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)




# Create your views here.
