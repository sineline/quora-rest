from rest_framework import serializers
from django.contrib.auth.models import User
from quora_api.models import (
    Question,
    Answer
)

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("This field may not be blank.")

        return value

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    author_name = serializers.SerializerMethodField()
    
    def get_author_name(self, obj):
        return obj.author.username

    # author = serializers.SerializerMethodField()
    # def get_author(self, obj):
    #     return obj.author.username

    class Meta:
        model = Question
        exclude = ('author',)
        #fields = "__all__"

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ('author', 'url_title',)
        #fields = "__all__"
