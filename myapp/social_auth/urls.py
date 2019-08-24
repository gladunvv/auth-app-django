from django.contrib import admin
from django.urls import path, include

from social_auth.views import (
    StartedScreenView,
    RequestFriendsView,
    LogoutView
)


urlpatterns = [
    path('', StartedScreenView.as_view(), name='started_screen'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('friends', RequestFriendsView.as_view(), name='friends')
]
