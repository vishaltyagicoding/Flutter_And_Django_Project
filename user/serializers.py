from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=CustomUser.objects.all())
            ], required=True
    )

    password = serializers.CharField(write_only=True,
                                    required=True, 
                                    validators=[validate_password],
                                    style={'input_type': 'password'})
    
    password2 = serializers.CharField(write_only=True,
                                       required=True,
                                       style={'input_type': 'password'})
    
    class Meta:
        model = CustomUser
        fields = ("email", "password", "password2")

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email']
        )
        
        user.set_password(validated_data['password'])
        user.save()

        return user


