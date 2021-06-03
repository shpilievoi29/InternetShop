from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from user.forms import UserSignUpForm, UserSignInForm
from django.shortcuts import render


def user_register(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get("username"),
                email=form.cleaned_data.get("email"),
                password=form.cleaned_data.get("password1"),
                first_name=form.cleaned_data.get("first_name"),
                last_name=form.cleaned_data.get("last_name"),

            )
            redirect_url = reverse_lazy("login")
            return HttpResponseRedirect(redirect_url)
    else:
        form = UserSignUpForm()
    context = {"form": form}
    return render(request, "user/register.html", context)


class UserSignUpView:
    ...


def user_login(request):
    if request.method == "POST":
        form = UserSignInForm(data=request.POST)
        if form.is_valid():
            # user = authenticate(username=form.cleaned_data.get("username"),
            #                     password=form.cleaned_data.get("password"))
            # if user is None:
            login(request, form.get_user())
            redirect_url = reverse_lazy("product_list")
            return HttpResponseRedirect(redirect_url)
    else:
        form = UserSignInForm()
    return render(request, "user/login.html", {"form": form})


def user_logout(request):
    logout(request)
    logout_redirect = reverse_lazy(request, "/")

    return HttpResponseRedirect(request, logout_redirect)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user/profile.html"
