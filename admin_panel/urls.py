from django.urls import path, include

from .views import (RoleListCreateAPIView, 
                    RoleRetrieveUpdateDestroyAPIView, 
                    QuestionListCreateAPIView, 
                    QuestionRetrieveUpdateDestroyAPIView)



urlpatterns = [
    path('admin/role/', RoleListCreateAPIView.as_view()),
    path('admin/role/<int:pk>/', RoleRetrieveUpdateDestroyAPIView.as_view()),
    path('admin/question/', QuestionListCreateAPIView.as_view()),
    path('admin/question/<int:pk>/', QuestionRetrieveUpdateDestroyAPIView.as_view()),
]