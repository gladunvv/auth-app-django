from django.contrib import admin
from django.urls import path, include
from social_auth.views import StartedScreenView

urlpatterns = [
    path('', StartedScreenView.as_view())
]
