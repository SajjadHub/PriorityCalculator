from django.urls import path
from .views import home_view, login_view, base_view, intake_view,\
        assignment_intake_view

urlpatterns = [
    path("", home_view, name="home"),
    path("login/", login_view, name="login"),
    path("intake/", intake_view, name="intake"),
    path("intake/<project>/", assignment_intake_view, name="assignment_intake"),
    path("base/", base_view, name="base")
]
