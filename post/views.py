from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView
from .models import Post, Like
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404, redirect


class PostView(LoginRequiredMixin, ListView):
    template_name = "post/post_list.html"
    # Postをモデルに指定
    model = Post
    # select_relatedを用いることで発行されたクエリによってユーザー情報とツイート情報がidをキーとして結合された状態のレコードが返ってくる
    # そのため{{Post.user}}{{Post.content}},{{Post.created_at}}で再度クエリを発行する必要がなくなり、N+1問題を解決できる
    queryset = Post.objects.select_related("user")


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/create.html"
    # Postモデルを指定
    model = Post
    # contentのみ表示
    fields = ['content']
    success_url = reverse_lazy('post:post_list')

    def form_valid(self, form):
        # フォームがエラーなく送信された際に発動するメソッド
        # データの受取・保存の役割を担う
        # self.request.userログインしているユーザー
        # form.instance.user：フォームを送ったユーザー
        # フォームを送ったユーザー情報にツイートボタンを押したユーザーを格納
        form.instance.user = self.request.user
        # super().で継承することでform_validのもともとの機能も保つ
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post/detail.html'
    queryset = Post.objects.select_related("user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_for_post_count = self.object.Like_set.count()
        # ポストに対するイイね数
        context['like_for_post_count'] = like_for_post_count
        # ログイン中のユーザーがイイねしているかどうか
        if self.object.Like_set.filter(user=self.request.user).exists():
            context['is_user_liked_for_post'] = True
        else:
            context['is_user_liked_for_post'] = False

        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'post/delete.html'
    model = Post
    success_url = reverse_lazy("post:home_list")


class LikeToggleView(LoginRequiredMixin, View):
    # **kwargs: URLパターンから渡される追加のキーワード引数。ここでは、post_idが含まれています。
    def post(self, request, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['post_id'])
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            like.delete()
            post.like_count -= 1
            liked = False
        else:
            post.like_count += 1
            liked = True

        post.save()

        return JsonResponse({'liked': liked, 'like_count': post.like_count})