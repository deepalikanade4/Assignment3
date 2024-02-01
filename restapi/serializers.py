from rest_framework import serializers
from .models import UserData


class UserDataSerializer(serializers.Serializer):
    UserID=serializers.IntegerField()
    Name=serializers.CharField(max_length=70)
    EmailID=serializers.EmailField(max_length=255)
    Designation=serializers.CharField(max_length=255)


    def create(self, validated_data):
        return UserData.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.UserID=validated_data.get('UserID',instance.UserID)
        instance.Name=validated_data.get('Name',instance.Name)
        instance.EmailID=validated_data.get('EmailID',instance.EmailID)
        instance.Designation=validated_data.get('Designation',instance.Designation)
        instance.save()
        return instance