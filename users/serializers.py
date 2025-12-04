from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        
        def validate(self, data):
            if data['password1'] != data['password2']:
                raise serializers.ValidationError("Passwords do not match.")


            validate_password(data['password1'])

            return data

    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
 
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "avatar"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()