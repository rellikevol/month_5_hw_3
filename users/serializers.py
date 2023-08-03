from rest_framework import serializers
from users.models import User
from todo.serializers import ToDoSerializer
from django.contrib.auth import password_validation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'age')


class UserDetailSerializer(serializers.ModelSerializer):
    user_task = ToDoSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'age', 'user_task')


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=30, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=30, write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email', 'phone_number', 'age')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})
        password_validation.validate_password(attrs['password'], self.instance)
        return attrs

    def create(self, validated_data: dict):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            age=validated_data['age']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
