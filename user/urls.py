from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import user_register, user_login, user_logout, UserProfileView

urlpatterns = [
    path("registration/", user_register, name="registration"),
    path("login/", user_login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile")
]