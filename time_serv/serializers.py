from rest_framework import serializers

class CurrentTimeSerializer(serializers.Serializer):
    current_time = serializers.DateTimeField()