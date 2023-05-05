from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from api.models import Role, Question
from api.serializers import RoleSerializer, QuestionSerializer

class RoleListCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True).data
        return Response(serializer)


    def create(self, request, *args, **kwargs):
        data = {**request.data}
        serializer = self.get_serializer(data=data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
        else:
            return Response({"error": "got wrong data"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_201_CREATED)


class RoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = [IsAdminUser]


    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Role.objects.get(pk=pk)
        except:
            return Response({"error":"does not exist this Role"}, status=status.HTTP_404_NOT_FOUND)
    
        data = {
            **request.data
        }

        serializer = self.get_serializer(instance=instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_205_RESET_CONTENT)


    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Role.objects.get(pk=pk)
        except:
            return Response({"error":"does not exist this Role"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]


    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True).data
        return Response(serializer)


    def create(self, request, *args, **kwargs):
        data = {**request.data}

        serializer = self.get_serializer(data=data)
        
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
        else:
            return Response({"error": "got wrong data"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_201_CREATED)


class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]


    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Question.objects.get(pk=pk)
        except:
            return Response({"error":"does not exist this Question"}, status=status.HTTP_404_NOT_FOUND)
    
        data = {
            **request.data
        }

        serializer = self.get_serializer(instance=instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_205_RESET_CONTENT)


    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Question.objects.get(pk=pk)
        except:
            return Response({"error":"does not exist this Question"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    