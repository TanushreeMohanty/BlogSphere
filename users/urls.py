from django.urls import path
from .views import home, register, login_view, logout_view

urlpatterns = [
    path("", home, name="blog-home"),  # Home Page
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
