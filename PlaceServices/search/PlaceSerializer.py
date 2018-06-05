from rest_framework import serializers
import json

class PlaceSerializer(serializers.Serializer):
    ID = serializers.CharField(max_length=255)
    Provider = serializers.CharField(max_length=255)
    Name = serializers.CharField(max_length=255)
    Description = serializers.CharField(max_length=255)
    #Location = PGHstoreField()
    Address = serializers.CharField(max_length=255)