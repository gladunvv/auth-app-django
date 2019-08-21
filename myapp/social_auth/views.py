from django.shortcuts import render, get_object_or_404
from social_django.models import UserSocialAuth

import requests

from django.views.generic import TemplateView


class StartedScreenView(TemplateView):
    template_name = "social_auth/base.html"


class RequestFriends(TemplateView):
    template_name = "social_auth/list_friends.html"

    def get(self, request, *args, **kwargs):
        COUNT = '5'
        METHOD_NAME = 'friends.get'
        VERSION_API = '5.101'
        if request.user.is_authenticated:
            user = UserSocialAuth.objects.get(pk=request.user.id)

            user_id = str(user.extra_data['id'])
            user_token = str(user.access_token)

            response = requests.get(
                "https://api.vk.com/method/friends.get?count=5&access_token=").json()

            # https://api.vk.com/method/{METHOD_NAME}?&count={COUNT}&access_token={user_token}&v={VERSION_API}".format(
            #     METHOD_NAME=METHOD_NAME,
            #     COUNT=COUNT,
            #     user_token=user_token,
            #     VERSION_API=VERSION_API
            # ))
            print(response)
            return render(request, self.template_name, context=response)
