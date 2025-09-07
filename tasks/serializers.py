from rest_framework import serializers
from django.utils import timezone
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('user', 'completed_at',)

    def validate_due_date(self, value):
        # prevent past dates
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def update(self, instance, validated_data):
        """
        Once a task is Completed, block edits to any fields
        unless status is being reverted to Pending.
        """
        current_status = instance.status
        new_status = validated_data.get('status', current_status)

        if current_status == 'Completed':
            # if not reverting to Pending, block any other field changes
            if new_status == 'Completed':
                changed_keys = set(validated_data.keys()) - {'status'}
                if changed_keys:
                    raise serializers.ValidationError(
                        "Completed tasks cannot be edited unless reverted to Pending."
                    )

        # if transitioning Pending -> Completed via normal update, set completed_at
        if current_status != 'Completed' and new_status == 'Completed' and instance.completed_at is None:
            instance.completed_at = timezone.now()

        return super().update(instance, validated_data)

        
