from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from api.models import Role, Question
from api.serializers import RoleSerializer, QuestionSerializer

class RoleViewset(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = [IsAdminUser]


class QuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]
