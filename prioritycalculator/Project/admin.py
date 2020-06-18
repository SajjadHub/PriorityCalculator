from django.contrib import admin

# Register your models here.

from .models import Project
from .models import Assignment

admin.site.register(Project)
admin.site.register(Assignment)
