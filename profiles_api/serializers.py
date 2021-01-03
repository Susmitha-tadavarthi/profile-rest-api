from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field to tes our APIviews"""
    name = serializers.CharField(max_length=10)
