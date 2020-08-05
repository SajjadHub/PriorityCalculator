from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProjectForm, AssignmentForm
from .models import Project, Assignment


def schedule_view(request, *args, **kwargs):
    """
    View for displaying top priority assignments
    """
    # Redirect if user is not logged into an account
    if request.user.is_anonymous:
        return redirect(reverse('login'))

    try:
        # Get all assignments for a user and sort them highest first
        activeuser = request.user
        data = sorted(Assignment.objects.filter(user=activeuser), key=lambda m:
                      -m.priority)
    except Assignment.DoesNotExist:
        # No data
        data = None

    context = {
            "data": data
            }
    return render(request, "schedule.html", context)


def assignment_intake_view(request, project="none", *args, **kwargs):
    """
    View for adding an assignment to project
    """
    # Redirect if user is not logged into an account
    if request.user.is_anonymous:
        return redirect(reverse('login'))

    # Assignment form
    form = AssignmentForm(request.POST or None)

    # If the form is valid assign it the active user and related project
    if form.is_valid():
        newAssignment = form.save()
        activeuser = request.user
        userproject = Project.objects.get(user=activeuser, name=project)
        newAssignment.project = userproject
        newAssignment.user = activeuser
        newAssignment.save()
        form = AssignmentForm()

    # Get and add to context all assignments for the given project and user
    # to display
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
    # Redirect if user is not logged into an account
    if request.user.is_anonymous:
        return redirect(reverse('login'))

    # In the special case of POST and the "Add assignment" button was clicked
    # the users project is saved and the user is redirected to the associated
    # assignment_intake_view
    if request.method == "POST" and "assig" in request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            newProject = form.save()
            newProject.user = request.user
            newProject.save()
            response = redirect(request.POST['name'] + '/', permanent=True)
            return response

    # For regular project form requests
    form = ProjectForm(request.POST or None)
    # If form is valid assign active user to the project and save
    if form.is_valid():
        newProject = form.save()
        newProject.user = request.user
        newProject.save()
        form = ProjectForm()

    # Get all projects for active user to display
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
    # Renders main page (home page)
    return render(request, "home.html", {})


def logout_success_view(request, *args, **kwargs):
    # View to logut user and send them a logout success page
    logout(request)
    return render(request, "logout_success.html")


def login_success_view(request, *args, **kwargs):
    # Renders a login success page
    return render(request, "login_success.html")


def login_view(request, *args, **kwargs):
    # View to take in a user login form and login the request
    # TODO:
    # - check if the user is already active to redirect them to logout first
    form = AuthenticationForm()
    form_result = None
    # Login the user if they are valid
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(request, username=username, password=password)

        # If the user is authenticated then log them in and redirect to success
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
    # View for adding a new user to system
    # TODO:
    # - Check if user is logged in first

    form_result = None
    # Get data with built in UserCreationForm, add the user, log them in
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
