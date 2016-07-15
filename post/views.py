# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect

from post.forms import PostForm
from post.models import Post, Categories


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


def likes_detail(request, id):
    post = Post.objects.get(id=id)
    post.likes += 1
    post.save()
    return redirect('/')


def dislikes_detail(request, id):
    post = Post.objects.get(id=id)
    post.dislikes += 1
    post.save()
    return redirect('/')


def create_category(request):
    if 'title' in request.GET and 'slug' in request.GET:
        category = Categories.objects.create(
            slug=request.GET['slug'], title=request.GET['title']
        )
        redirect_url = '/category/%s/' % category.slug
        return redirect(redirect_url)
    return render(request, 'post/create_category.html', {})


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'post/create_post.html', {'form': form})




