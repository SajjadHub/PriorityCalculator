from django.urls import path
from .views import home_view, login_view, base_view, intake_view,\
        assignment_intake_view, login_success_view, signup_view,\
        logout_success_view, schedule_view

urlpatterns = [
    path("", home_view, name="home"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("login/success/", login_success_view, name="login_success"),
    path("logout/success/", logout_success_view, name="logout_success"),
    path("intake/", intake_view, name="intake"),
    path("intake/<project>/", assignment_intake_view, name="assignment_intake"),
    path("schedule/", schedule_view, name="schedule"),
    path("base/", base_view, name="base")
]
