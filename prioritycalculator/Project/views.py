from django.shortcuts import render, get_object_or_404
from .forms import ProjectForm, AssignmentForm
from .models import Project, Assignment

# Create your views here.


def assignment_intake_view(request, project="none", *args, **kwargs):
    form = AssignmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AssignmentForm()

    try:
        data = Assignment.objects.get(projectName=project)
    except Assignment.DoesNotExist:
        data = None

    context = {
            'form': form,
            'data': data
            }
    return render(request, "assignment_intake.html", context)


def intake_view(request, project="none", *args, **kwargs):
    print(request)
    if 'assig' in request.POST:
        assignment_intake_view(request, project)
    else:
        print(request.POST)
        form = ProjectForm(request.POST or None)
        data = Project.objects.all()
        if form.is_valid():
            form.save()
            form = ProjectForm()

        context = {
                'form': form,
                'data': data
                }
        return render(request, "intake.html", context)


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})


def base_view(request, *args, **kwargs):
    return render(request, "base.html", {})
