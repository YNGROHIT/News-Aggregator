from django.urls import path
from .views import register_view, login_view, logout_view, index, home

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("", index, name="index"),
    path('home/', home, name='home'),
]
