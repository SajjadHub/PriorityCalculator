from django import forms

from .models import Project, Assignment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = {
                'name',
                'weight'
                }


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = {
                'projectName',
                'name',
                'weight',
                'deadline'
                }
