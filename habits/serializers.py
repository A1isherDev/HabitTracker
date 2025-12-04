from rest_framework import serializers
from habits.models import Habits

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = ["id", "title", "icon", "frequency", "color", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_frequency(self, value):
        if value < 1 or value > 7:
            raise serializers.ValidationError("Weekdays must be between 1 and 7.")
        return value
