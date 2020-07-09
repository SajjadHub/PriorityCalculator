from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=60)
    weight = models.IntegerField()

    def __str__(self):
        return self.name


class Assignment(models.Model):
    projectName = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    weight = models.IntegerField()
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    priority = models.DecimalField(max_digits=5,
                                   decimal_places=2,
                                   default=-1.0)

    def __str__(self):
        return self.name
