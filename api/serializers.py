from rest_framework import serializers

from .models import Role, Question


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name','url_to_program', 'description', 'video')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question','positive_choice', 'negative_choice', 'point', 'role')