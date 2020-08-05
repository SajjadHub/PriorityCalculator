from django.contrib import admin

# Register your models here.
"""
Importing Project (holds information on projects: name, weight, user)
and on Assignment (info on assignments: user, project, name, weight,
deadline, completed, priority)
"""
from .models import Project
from .models import Assignment

admin.site.register(Project)
admin.site.register(Assignment)
