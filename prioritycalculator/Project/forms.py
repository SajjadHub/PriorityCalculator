from django import forms

from .models import Project, Assignment


class ProjectForm(forms.ModelForm):
    """
    Form for adding a project to a users list
    Note: user is assigned in intake_view
    """
    class Meta:
        model = Project
        fields = {
                'name',
                'weight'
                }
    # specifies order the form appears in html
    field_order = ['name', 'weight']


class AssignmentForm(forms.ModelForm):
    """
    Form for adding assignment to a user project
    Note: user and project are assigned in intake_view
    Note: priority calculated as property
    """
    class Meta:
        model = Assignment
        fields = {
                'name',
                'weight',
                'deadline'
                }
    field_order = ['name', 'weight', 'deadline']
