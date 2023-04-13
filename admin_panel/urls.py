from django.urls import path, include

from rest_framework import routers

from .views import RoleViewset, QuestionViewset


router = routers.DefaultRouter()
router.register(r'role',RoleViewset)
router.register(r'question', QuestionViewset)

urlpatterns = [
    path('admin/', include(router.urls))
]