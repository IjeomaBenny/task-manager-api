from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # Include all fields
        fields = '__all__'
        # Make 'user' and 'completed_at' read-only
        read_only_fields = ('user', 'completed_at',)

    def validate_due_date(self, value):
        """
        Ensure the due date is not in the past.
        """
        from django.utils import timezone
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

        
