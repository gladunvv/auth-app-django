from django.shortcuts import render
from django.views.generic import TemplateView


class StartedScreenView(TemplateView):
    template_name = "social_auth/base.html"
