from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import logout

from social_django.models import UserSocialAuth
from social_auth.api_requests import vk_api_requests


class StartedScreenView(TemplateView):
    """Класс стартового экрана приложения, где проходит проверка на авторизацию"""

    template_name = "social_auth/started_screen.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('friends')
        else:
            return render(request, self.template_name)


class RequestFriendsView(TemplateView):
    """Основной класс приложения для идентификации пользователя и запроса к ВК API"""

    template_name = "social_auth/list_friends.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = UserSocialAuth.objects.get(user=request.user)
            user_token = user.access_token
            user_vk = vk_api_requests(user_token, method='users.get')
            friends = vk_api_requests(user_token, method='friends.get')
            context = {
                "user": user_vk['response'][0],
                "friends": friends['response']
            }

            return render(request, self.template_name, context=context)
        else:
            return HttpResponseRedirect('/')


class LogoutView(TemplateView):
    """Класс отвечающий за выход из приложения"""

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
