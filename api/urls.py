from django.urls import path

from . import views

urlpatterns = [
    path('role/', views.RoleAPIView.as_view()),
    path('questions/', views.QuestionListApiList.as_view()),
]