from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProjectForm, AssignmentForm
from .models import Project, Assignment


def schedule_view(request, *args, **kwargs):
    if request.user.is_anonymous:
        return redirect(reverse('login'))

    try:
        activeuser = request.user
        data = sorted(Assignment.objects.filter(user=activeuser), key=lambda m: -m.priority)
    except Assignment.DoesNotExist:
        data = None

    context = {
            "data": data
            }
    return render(request, "schedule.html", context)


def assignment_intake_view(request, project="none", *args, **kwargs):
    # to deal with those not logged in
    if request.user.is_anonymous:
        return redirect(reverse('login'))

    form = AssignmentForm(request.POST or None)

    if form.is_valid():
        newAssignment = form.save()
        activeuser = request.user
        userproject = Project.objects.get(user=activeuser, name=project)
        newAssignment.project = userproject
        newAssignment.user = activeuser
        newAssignment.save()
        form = AssignmentForm()

    try:
        activeuser = request.user
        userproject = Project.objects.filter(user=activeuser, name=project)
        data = Assignment.objects.filter(user=activeuser, project__in=userproject)
    except Assignment.DoesNotExist:
        data = None

    context = {
            'form': form,
            'data': data,
            'project': project
            }
    return render(request, "assignment_intake.html", context)


def intake_view(request, *args, **kwargs):
    if request.user.is_anonymous:
        return redirect(reverse('login'))
    if request.method == "POST" and "assig" in request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            newProject = form.save()
            newProject.user = request.user
            newProject.save()
            response = redirect(request.POST['name'] + '/', permanent=True)
            return response

    form = ProjectForm(request.POST or None)
    if form.is_valid():
        newProject = form.save()
        newProject.user = request.user
        newProject.save()
        form = ProjectForm()

    try:
        data = Project.objects.filter(user=request.user)
    except Project.DoesNotExist:
        data = None

    context = {
            'form': form,
            'data': data
            }
    return render(request, "intake.html", context)


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def logout_success_view(request, *args, **kwargs):
    logout(request)
    return render(request, "logout_success.html")


def login_success_view(request, *args, **kwargs):
    return render(request, "login_success.html")


def login_view(request, *args, **kwargs):
    form = AuthenticationForm()
    form_result = None
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = redirect("success/", permanent=True)
            return response
        else:
            form_result = "Invalid username or password"
    content = {
            "form": form,
            "form_result": form_result
            }

    return render(request, "login.html", content)


def signup_view(request, *args, **kwargs):
    form_result = None
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('home'))
        else:
            form_result = "Invalid"
    form = UserCreationForm()
    context = {
            "form": form,
            "form_result": form_result
            }
    return render(request, "signup.html", context)


def base_view(request, *args, **kwargs):
    return render(request, "base.html", {})
