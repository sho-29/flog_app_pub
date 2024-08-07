from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    questions_num = models.IntegerField(default=0)
    answered_question_num = models.IntegerField(default=0)
    correct_num = models.IntegerField(default=0)
    incorrect_num = models.IntegerField(default=0)
    correct_rate = models.IntegerField(default=0)
    total_correct_rate = models.IntegerField(default=0)

    def player_result(self, correct_rate):
        self.correct_rate = correct_rate
        return correct_rate
