# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect

from post.forms import PostForm
from post.models import Post, Categories
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    query = request.GET.get('query')
    if query:
        posts = posts.filter(text__icontains=query)
    return render(request, 'post/post_list.html', {
        'posts': posts, 'query':query
    })


def post_detail(request, info_id):
    posts = Post.objects.get(pk=info_id)
    return render(request, "post/post_detail.html", {'posts': posts})


@login_required(login_url='/')
def likes_detail(request, id):
    post = Post.objects.get(id=id)
    post.likes += 1
    post.save()
    return redirect('/')


@login_required(login_url='/')
def dislikes_detail(request, id):
    post = Post.objects.get(id=id)
    post.dislikes += 1
    post.save()
    return redirect('/')


@login_required
def create_category(request):
    if request.user.is_staff:
        if 'title' in request.GET and 'slug' in request.GET:
            category = Categories.objects.create(
                slug=request.GET['slug'], title=request.GET['title']
            )
            redirect_url = '/category/%s/' % category.slug
            return redirect(redirect_url)
    return render(request, 'post/create_category.html', {})


@login_required
def create_post(request):
    form = PostForm()
    if request.user.is_staff:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
    return render(request, 'post/create_post.html', {'form': form})


def update_post(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(
        request.POST or None, request.FILES or None, instance=post
    )
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'post/create_post.html', {'form': form})


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')



