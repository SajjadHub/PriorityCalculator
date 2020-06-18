from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=60)
    weight = models.IntegerField()


class Assignment(models.Model):
    projectName = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    weight = models.IntegerField()
    deadline = models.DateField()
