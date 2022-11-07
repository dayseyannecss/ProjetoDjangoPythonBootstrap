from django.urls import path
from django.contrib.auth import views as authviews



urlpatterns = [
    path("login", authviews.LoginView.as_view(
        template_name='users/login.html'
    ), name="login"),

    path("logout", authviews.LogoutView.as_view(
        template_name='users/login.html'
    ), name="logout"),
]
