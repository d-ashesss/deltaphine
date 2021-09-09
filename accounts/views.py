from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import views as auth_views
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView

def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("accounts:profile")
    return auth_views.LoginView.as_view(extra_context={"title": "Login"})(request)

def logout(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("index")
    return auth_views.LogoutView.as_view()(request)

@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = "registration/profile.html"
    extra_context = {"title": "Profile"}
