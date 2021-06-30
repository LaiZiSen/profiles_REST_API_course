from django.db.models.fields import TextField
from rest_framework import serializers


class HelloSerialiser(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)