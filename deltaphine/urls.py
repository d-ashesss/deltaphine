"""
URL configuration for deltaphine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, reverse
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

def login(request):
    if request.user.is_authenticated:
        return redirect("profile")
    return auth_views.LoginView.as_view(extra_context={"title": "Login"})(request)

def logout(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("index")
    return auth_views.LogoutView.as_view()(request)

@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = "registration/profile.html"
    extra_context = {"title": "Profile"}

urlpatterns = [
    path('', TemplateView.as_view(template_name="base.html"), name='index'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path("accounts/login/", login, name="login"),
    path("accounts/logout/", logout, name="logout"),
    path('admin/', admin.site.urls),
]
