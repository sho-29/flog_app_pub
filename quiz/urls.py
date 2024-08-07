from django.urls import path

from . import views

app_name = "quiz"

urlpatterns = [
    path('question_invite/', views.question_invite_view, name='question_invite'),
    path('question_date/', views.question_date_view, name='question_date'),
    path('question_confession/', views.question_confession_view, name='question_confession'),
    path('result_invite/', views.result_invite_view, name='result_invite'),
    path('result_date/', views.result_date_view, name='result_date'),
    path('result_confession/', views.result_confession_view, name='result_confession'),
]
