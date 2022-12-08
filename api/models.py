from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(verbose_name="name of IT proffesion",max_length=64, unique=True)
    description = models.TextField(default='emty', verbose_name="About this proffesion")
    video = models.URLField(verbose_name="link to some video about this proffesion")


    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(verbose_name="write a question in here field")
    point = models.IntegerField(default=1)
    role = models.ForeignKey(Role, to_field="name",verbose_name="select where this question to be", on_delete=models.CASCADE)


    def __str__(self):
        return self.name[:10] + "..."