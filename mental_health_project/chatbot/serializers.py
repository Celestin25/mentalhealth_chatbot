from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ChatHistory

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class ChatHistorySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = ChatHistory
        fields = ('id', 'message', 'response', 'language', 'timestamp', 'username')

    def get_username(self, obj):
        return obj.user.username