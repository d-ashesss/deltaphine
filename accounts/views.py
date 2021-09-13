from typing import Any
from django import http
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import views as auth_views
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView, FormView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .forms import ProfileForm


def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("accounts:profile")
    return auth_views.LoginView.as_view(extra_context={"title": _("Login")})(request)


def logout(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("index")
    return auth_views.LogoutView.as_view()(request)


@method_decorator(login_required, name="dispatch")
class ProfileView(FormView):
    template_name = "registration/profile.html"
    form_class = ProfileForm
    extra_context = {"title": _("Profile")}
    success_url = "."

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"instance": self.request.user})
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
