from django.contrib import admin
from .models import Quiz_invite,Quiz_date,Quiz_confession, Player_result
# Register your models here.
# モデルをimportし、admin.site.register(モデル名)を記述することで管理者サイトにモデルを表示することができる
admin.site.register(Quiz_invite)
admin.site.register(Quiz_date)
admin.site.register(Quiz_confession)
admin.site.register(Player_result)
