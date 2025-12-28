from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    # 主页和文章列表
    path('', views.index, name='index'),

    # 文章相关
    path('new/', views.new_post, name='new_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),

    # 用户相关
    path('register/', views.register, name='register'),
    path('user/<str:username>/', views.user_posts, name='user_posts'),
]