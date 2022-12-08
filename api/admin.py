from django.contrib import admin

from .models import Role, Question
# Register your models here.
admin.site.register(Role)
admin.site.register(Question)