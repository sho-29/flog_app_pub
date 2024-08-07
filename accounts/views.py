from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.urls import reverse_lazy
from quiz.models import Player_result
from django.shortcuts import render, redirect
from django.db.models import Max, Min
from .forms import SignupForm, UserUpdateForm
User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Use password1 for password field
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy(settings.LOGIN_REDIRECT_URL))  # Redirect to the success URL
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_profile_view(request, username):
    user = User.objects.get(username=username)  
    # usernameフィールドと受け取った入力値が等しくなるような行を抽出
    player_result = Player_result.objects.filter(user=user)
    print(player_result)
    # __gt=0で０より大きいレコードのみを抽出
    max_rate_invite = player_result.filter(flog_rate_invite__gt=0).aggregate(Max('flog_rate_invite'))['flog_rate_invite__max']
    max_rate_date = player_result.filter(flog_rate_date__gt=0).aggregate(Max('flog_rate_date'))['flog_rate_date__max']
    max_rate_confession = player_result.filter(flog_rate_confession__gt=0).aggregate(Max('flog_rate_confession'))['flog_rate_confession__max']
    min_rate_invite = player_result.filter(flog_rate_invite__gt=0).aggregate(Min('flog_rate_invite'))['flog_rate_invite__min']
    min_rate_date = player_result.filter(flog_rate_date__gt=0).aggregate(Min('flog_rate_date'))['flog_rate_date__min']
    min_rate_confession = player_result.filter(flog_rate_confession__gt=0).aggregate(Min('flog_rate_confession'))['flog_rate_confession__min']
    print(max_rate_invite)
    params = {
        'player_result': player_result,
        'username': username,
        'max_rate_invite': max_rate_invite,
        'max_rate_date': max_rate_date,
        'max_rate_confession': max_rate_confession,
        'min_rate_invite': min_rate_invite,
        'min_rate_date': min_rate_date,
        'min_rate_confession': min_rate_confession
    }
    return render(request, 'accounts/user_profile.html', params)


def user_edit_view(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        user_form = UserUpdateForm(request.POST, instance=user)
        # password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            url = reverse_lazy('accounts:user_profile',
                               kwargs={'username': username})
            # password_form.save()
            # update_session_auth_hash(request, password_form.user)
            # username=usernameで更新後にユーザーごとのプロフィールページにリダイレクト
            return redirect(url, username=username)
    else:
        user = User.objects.get(username=username)
        user_form = UserUpdateForm(instance=user)
        # password_form = PasswordChangeForm(request.user)

    params = {
        'user_form': user_form,
        # 'password_form': password_form,
    }
    return render(request, 'accounts/edit.html', params)
