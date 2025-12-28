from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import BlogPost
from .forms import BlogPostForm, CustomUserCreationForm


def index(request):
    """显示所有博客文章的主页"""
    search_query = request.GET.get('q', '')

    if search_query:
        posts = BlogPost.objects.filter(
            Q(title__icontains=search_query) |
            Q(text__icontains=search_query) |
            Q(owner__username__icontains=search_query)
        ).order_by('-date_added')
    else:
        posts = BlogPost.objects.all().order_by('-date_added')

    # 分页：每页显示5篇文章
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_posts': posts.count(),
    }
    return render(request, 'blogs/index.html', context)


@login_required
def new_post(request):
    """创建新博客文章"""
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            messages.success(request, '博客文章已成功发布！')
            return redirect('blogs:index')
        else:
            messages.error(request, '请检查表单中的错误。')
    else:
        form = BlogPostForm()

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """编辑现有博客文章"""
    post = get_object_or_404(BlogPost, id=post_id)

    # 检查用户是否有权限编辑此文章
    if post.owner != request.user:
        messages.error(request, '您没有权限编辑这篇文章。')
        return redirect('blogs:index')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, '博客文章已成功更新！')
            return redirect('blogs:index')
        else:
            messages.error(request, '请检查表单中的错误。')
    else:
        form = BlogPostForm(instance=post)

    context = {
        'form': form,
        'post': post,
        'is_edit': True,
    }
    return render(request, 'blogs/edit_post.html', context)


@login_required
def delete_post(request, post_id):
    """删除博客文章"""
    post = get_object_or_404(BlogPost, id=post_id)

    # 检查用户是否有权限删除此文章
    if post.owner != request.user:
        messages.error(request, '您没有权限删除这篇文章。')
        return redirect('blogs:index')

    if request.method == 'POST':
        post.delete()
        messages.success(request, '博客文章已成功删除！')
        return redirect('blogs:index')

    context = {'post': post}
    return render(request, 'blogs/delete_confirm.html', context)


def register(request):
    """用户注册"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # 自动登录新用户
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, f'欢迎 {username}！您已成功注册并登录。')
            return redirect('blogs:index')
        else:
            messages.error(request, '请检查表单中的错误。')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'blogs/register.html', context)


def post_detail(request, post_id):
    """查看文章详情"""
    post = get_object_or_404(BlogPost, id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post_detail.html', context)


def user_posts(request, username):
    """查看指定用户的所有文章"""
    from django.contrib.auth.models import User
    user = get_object_or_404(User, username=username)
    posts = BlogPost.objects.filter(owner=user).order_by('-date_added')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'profile_user': user,
        'total_posts': posts.count(),
    }
    return render(request, 'blogs/user_posts.html', context)