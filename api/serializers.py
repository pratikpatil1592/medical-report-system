from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import CustomUser, FileUpload

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_staff', 'name', 'age', 'address', 'patient_name', 'patient_relation', 'phone_number')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'is_staff', 'name', 'age', 'address', 'patient_name', 'patient_relation', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'], 
            validated_data['email'], 
            validated_data['password'], 
            is_staff=validated_data['is_staff'], 
            name=validated_data['name'], 
            age=validated_data['age'], 
            address=validated_data['address'], 
            patient_name=validated_data['patient_name'], 
            patient_relation=validated_data['patient_relation'], 
            phone_number=validated_data['phone_number']
        )
        return user


# File Upload Serializer
class FileUploadSerializer(serializers.ModelSerializer):
  class Meta():
    model = FileUpload
    fields = ('file', 'user', 'filetype', 'description', 'timestamp')