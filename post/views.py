from django.shortcuts import render, redirect

from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {
        'posts': posts
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