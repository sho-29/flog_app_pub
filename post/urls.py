from django.urls import path
from . import views
app_name = 'post'
urlpatterns = [
    path("post/", views.PostView.as_view(), name="post_list"),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:post_id>/like/', views.LikeToggleView.as_view(), name='post_like'),
    ]
