from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjectForm, AssignmentForm
from .models import Project, Assignment

# Create your views here.


def assignment_intake_view(request, project="none", *args, **kwargs):
    form = AssignmentForm(request.POST or None)
    if form.is_valid():
        full_form = form.save()
        full_form.projectName = project
        full_form.save()
        form = AssignmentForm()

    try:
        data = Assignment.objects.filter(projectName=project)
    except Assignment.DoesNotExist:
        data = None

    context = {
            'form': form,
            'data': data,
            'project': project
            }
    return render(request, "assignment_intake.html", context)


def intake_view(request, *args, **kwargs):
    print(request, request.POST)
    if request.method == "POST" and "assig" in request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            response = redirect(request.POST['name'] + '/', permanent=True)
            print(response)
        return response

    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectForm()

    try:
        data = Project.objects.all()
    except Project.DoesNotExist:
        data = None

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
