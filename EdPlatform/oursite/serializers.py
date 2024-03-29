from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Course, Module, ImageForUser, Homework, User, Constructor, Content, Message,Notifications, Post

class ConstructorSerializerOfCurrentUser(serializers.ModelSerializer):
    # username = serializers.CharField()

    class Meta:
        model = Constructor
        fields = '__all__'

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'author')

class LoginSerializer(serializers.Serializer):


    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    def getSession(self, request):
        return request.session



        raise serializers.ValidationError("Incorrect Credentials")

class ShowImageUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageForUser
        fields = ('image',)

class ConstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constructor
        fields = ('id', 'title', 'description', 'slug', 'owner')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'owner', 'overview', 'created', 'url_to_course', 'url_to_catalog', 'url_to_catalog_buy')