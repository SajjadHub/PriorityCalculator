from django.urls import path
from .views import home_view, login_view, base_view, intake_view,\
        assignment_intake_view, login_success_view, signup_view,\
        logout_success_view, schedule_view

urlpatterns = [
    # home webpage
    path("", home_view, name="home"),

    # pages associated with users and authentication: login, logout, signup
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("login/success/", login_success_view, name="login_success"),
    path("logout/success/", logout_success_view, name="logout_success"),

    # pages for project intake, and assignment intake respectively
    path("intake/", intake_view, name="intake"),
    path("intake/<project>/", assignment_intake_view, name="assignment_intake"),

    # page for finalized assignment display
    path("schedule/", schedule_view, name="schedule"),

    # testing
    path("base/", base_view, name="base")
]
