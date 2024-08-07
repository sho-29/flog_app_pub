from .models import Quiz_date, Quiz_invite, Quiz_confession, Player_result
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


def question_invite_view(request):
    questions = Quiz_invite.objects.all()
    params = {
            'user': request.user,
            'questions': questions,
        }
    return render(request, 'quiz/question_invite.html', params)


def question_date_view(request):
    questions = Quiz_date.objects.all()
    params = {
            'user': request.user,
            'questions': questions,
        }
    return render(request, 'quiz/question_date.html', params)


def question_confession_view(request):
    questions = Quiz_confession.objects.all()
    params = {
            'user': request.user,
            'questions': questions,
        }
    return render(request, 'quiz/question_confession.html', params)


def result_invite_view(request):
    if request.method == 'POST':
        questions = Quiz_invite.objects.all()
        situaton1_score = 0
        correct = 0
        answered_num_invite = 0
        situation1_list = []
        player = request.user
        for q in questions:
            answered_num_invite += 1
            print(request.POST.get(q.question))
            if q.op1 == request.POST.get(q.question):
                situaton1_score += 0
                correct += 1
                situation1_list.append("great")
            elif q.op2 == request.POST.get(q.question):
                situaton1_score += 1
                situation1_list.append("good")
            elif q.op3 == request.POST.get(q.question):
                situaton1_score += 2
                situation1_list.append("frog")
            elif q.op4 == request.POST.get(q.question):
                situaton1_score += 3
                situation1_list.append("super frog")
        percent = situaton1_score/(answered_num_invite*3) * 100
        if percent == 0:
            percent = 1
        else:
            pass
        # Player_resultのデータを変数に格納
        player_result_invite = Player_result.objects.create(user=player, flog_rate_invite=percent)
        print(Player_result.objects.all().values())
        # 変数にsave()メソッドを適用してデータベースに保存
        player_result_invite.save()

        percent = player.player_result(percent)
        player.save()
        params = {
            'percent': int(percent),
            'questions': questions,
            'answered_num': answered_num_invite,
            'situation1_list': situation1_list,
        }
        return render(request, 'quiz/result_invite.html', params)

    else:
        params = {
            'user': request.user,
        }
        return render(request, 'quiz/question_invite.html', params)


def result_date_view(request):
    if request.method == 'POST':
        questions = Quiz_date.objects.all()
        situaton2_score = 0
        correct = 0
        answered_num_date = 0
        situation2_list = []
        player = request.user
        for q in questions:
            answered_num_date += 1
            print(request.POST.get(q.question))
            if q.op1 == request.POST.get(q.question):
                situaton2_score += 0
                correct += 1
                situation2_list.append("great")
            elif q.op2 == request.POST.get(q.question):
                situaton2_score += 1
                situation2_list.append("good")
            elif q.op3 == request.POST.get(q.question):
                situaton2_score += 2
                situation2_list.append("frog")
            elif q.op4 == request.POST.get(q.question):
                situaton2_score += 3
                situation2_list.append("super frog")
        percent = situaton2_score/(answered_num_date*3) * 100
        if percent == 0:
            percent = 1
        else:
            pass
        # Player_resultのデータを変数に格納
        player_result_date = Player_result.objects.create(user=player, flog_rate_date=percent)
        print(Player_result.objects.all().values())
        # 変数にsave()メソッドを適用してデータベースに保存
        player_result_date.save()

        percent = player.player_result(percent)
        player.save()
        params = {
            'percent': int(percent),
            'questions': questions,
            'answered_num_date': answered_num_date,
            'situation2_list': situation2_list,
        }
        return render(request, 'quiz/result_date.html', params)

    else:
        params = {
            'user': request.user,
        }
        return render(request, 'quiz/question_date.html', params)


def result_confession_view(request):
    if request.method == 'POST':
        questions = Quiz_confession.objects.all()
        situaton3_score = 0
        correct = 0
        answered_num_confession = 0
        situation3_list = []
        player = request.user
        for q in questions:
            answered_num_confession += 1
            print(request.POST.get(q.question))
            if q.op1 == request.POST.get(q.question):
                situaton3_score += 0
                correct += 1
                situation3_list.append("great")
            elif q.op2 == request.POST.get(q.question):
                situaton3_score += 1
                situation3_list.append("good")
            elif q.op3 == request.POST.get(q.question):
                situaton3_score += 2
                situation3_list.append("frog")
            elif q.op4 == request.POST.get(q.question):
                situaton3_score += 3
                situation3_list.append("super frog")
        percent = situaton3_score/(answered_num_confession*3) * 100
        if percent == 0:
            percent = 1
        else:
            pass
        # Player_resultのデータを変数に格納
        player_result_confession = Player_result.objects.create(user=player,
                                                                flog_rate_confession=percent)
        print(Player_result.objects.all().values())
        # 変数にsave()メソッドを適用してデータベースに保存
        player_result_confession.save()

        percent = player.player_result(percent)
        player.save()
        params = {
            'percent': int(percent),
            'questions': questions,
            'answered_num_confession': answered_num_confession,
            'situation3_list': situation3_list
        }
        return render(request, 'quiz/result_confession.html', params)

    else:
        params = {
            'user': request.user, 
        }
        return render(request, 'quiz/question_confession.html', params)
