from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import generics, status

from .models import Role, Question
from .serializers import RoleSerializer, QuestionSerializer

class QuestionListApiList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RoleAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        answer = request.data

        try:
            max_value = max(list(answer.values()))
            role = list(answer.keys())[list(answer.values()).index(max_value)]
            queryset = Role.objects.get(name = role)
        except:
            return Response("Not found role", status=status.HTTP_404_NOT_FOUND)
        
        serializer = RoleSerializer(queryset)
        return Response(serializer.data)