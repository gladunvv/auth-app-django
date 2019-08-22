from django.contrib import admin
from django.urls import path, include
from social_auth.views import StartedScreenView, RequestFriends

urlpatterns = [
    path('', StartedScreenView.as_view()),
    path('friends', RequestFriends.as_view(), name='friends')

]
