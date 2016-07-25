# coding: utf-8
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect('/')
            else:
                return redirect('accounts/login/')
        else:
            return redirect('/')