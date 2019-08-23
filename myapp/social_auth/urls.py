from django.contrib import admin
from django.urls import path, include
from social_auth.views import StartedScreenView, RequestFriends, LogoutView

urlpatterns = [
    path('', StartedScreenView.as_view(), name='starteds_screen'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('friends', RequestFriends.as_view(), name='friends')
]
