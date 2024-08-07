from django.db import models
from django.conf import settings


class Quiz_invite(models.Model):
    """クイズの問題を表すモデル"""
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    explanation = models.TextField(null=True)

    def __str__(self):
        return self.question


class Quiz_date(models.Model):
    """クイズの問題を表すモデル"""
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    explanation = models.TextField(null=True)

    def __str__(self):
        return self.question


class Quiz_confession(models.Model):
    """クイズの問題を表すモデル"""
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    explanation = models.TextField(null=True)

    def __str__(self):
        return self.question


class Player_result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    flog_rate_invite = models.IntegerField(default=0)
    flog_rate_date = models.IntegerField(default=0)
    flog_rate_confession = models.IntegerField(default=0)
