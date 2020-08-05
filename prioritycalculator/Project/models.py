from django.conf import settings
from django.db import models
import datetime

# Create your models here.

User = settings.AUTH_USER_MODEL


class Project(models.Model):
    """
    Defines the structure of a user project (course)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="project", null=True)
    name = models.CharField(max_length=60)
    weight = models.IntegerField()

    def __str__(self):
        return self.name


class Assignment(models.Model):
    """
    Defines the structure of a user assignment (lab, midterm, final, report...)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                null=True)
    name = models.CharField(max_length=60)
    weight = models.IntegerField()
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    priority = models.DecimalField(max_digits=10,
                                   decimal_places=2,
                                   default=-1.0)

    def __str__(self):
        return self.name

    @property
    def priority(self):
        """
        Calculates the priority based on the associated projects weight,
        days from deadline, and its own weight
        Note: @property is so that it is auto-calculated upon request
        TODO:
        - Modify priority calculation
        """
        projectweight = self.project.weight
        today = datetime.date.today()
        diff = self.deadline - today

        # self.priority = projectweight * self.weight * (1 / diff.days)
        return projectweight * self.weight * (1 / diff.days)
