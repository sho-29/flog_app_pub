from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:50]


class Like(models.Model):
    """いいねモデル"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='投稿', on_delete=models.CASCADE)

    class Meta:
        # 特定のユーザーが特定の投稿に対して一度だけ「いいね」を付けられるようにします。
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="like_unique"  # 制約の名前
                # データベース上で制約を特定するために記述する
            ),
        ]

