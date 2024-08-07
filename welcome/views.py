from quiz.models import Player_result
from django.shortcuts import render

from django.contrib.auth import get_user_model


User = get_user_model()


def welcome_view(request):
    params = {
        'user': request.user,
    }
    return render(request, 'welcome/welcome.html', params)
