from django.db.models import fields
from jiji.models import Product,User,Interests
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django import forms
    
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = Interests


class ProductSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True,read_only=True)
    
    class Meta:
        fields ='__all__'
        model = Product


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','state_of_residence','password', 'password2',)
        extra_kwargs = {
            'first_name': {'required':True},
            'last_name': {'required':True},
            'email': {'required': True},
            'state_of_residence':{'required':True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
