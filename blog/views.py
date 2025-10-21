#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import LoginForm, PostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from datetime import datetime
from django.urls import reverse
from .utils.utils import UtilsClass

# ------------------------------------------------------------------------------------- #

utils = UtilsClass()

# ------------------------------------------------------------------------------------- #

def home(request):
    if request.method == "POST":
        search_term = request.POST.get('search', '')
        posts = Post.objects.filter(title__icontains=search_term).order_by('-create_at')
        if not posts.exists():
            messages.warning(request, 'No articles were found with these titles.')

        paginator = Paginator(posts, 7)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

    else:
        posts = Post.objects.all().order_by('-create_at')
        paginator = Paginator(posts, 7)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

    postLast = posts.object_list[:1]
    post2 = posts.object_list[1:5]
    post3 = posts.object_list[5:8]

    return render(request, 'home/home.html', {
        'postsAll': posts,
        'postLast': postLast,
        'post2': post2,
        'post3': post3
    })

# ------------------------------------------------------------------------------------- #

def show(request, id):
    post = get_object_or_404(Post, id=id)
    author_name = f'{post.author.first_name} {post.author.last_name}'.strip() or post.author.username
    return render(request, "post/show.html", {'post': post, 'author_name': author_name})

@login_required(login_url="/login/")
def create(request):
    if request.method == 'POST':
        frm = PostForm(request.POST, request.FILES)
        if frm.is_valid():
            post = frm.save(commit=False)
            post.author = request.user
            post.create_at = datetime.now()
            post.update_at = None
            post.picture = request.FILES['picture']  # temporary!
            post.save()
            messages.success(request, 'Successfully created.')
            return HttpResponseRedirect(reverse('home'))
    else:
        frm = PostForm()
    return render(request, 'post/form.html', {'form': frm, 'edition':False, 'author_name' : utils.get_author_name(request.user)})

@login_required(login_url='/login/')
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    create_at = post.create_at
    if request.user.id == post.author_id:
        if request.method == 'POST':
            frm = PostForm(request.POST, request.FILES, instance=post)
            if frm.is_valid():
                post = frm.save(commit=False)
                post.author = request.user
                post.create_at = create_at

                # temporary!
                if request.FILES.get('picture'):  # if 'picture' is not empty
                    post.picture = request.FILES['picture']  # temporary!

                post.update_at = datetime.now()
                post.save()
                messages.success(request, 'Successfully edited.')
                return render(request, 'post/show.html', {'post': post})
            else:
                return render(request, 'post/form.html', {
                    'form': frm,
                    'post_id': id,
                    'edition': True,
                    'author_name': utils.get_author_name(request.user)
                })
        else:
            frm = PostForm(instance=post)
            return render(request, 'post/form.html', {
                'form': frm,
                'post_id': id,
                'edition': True,
                'author_name': utils.get_author_name(request.user)
            })
    else:
        messages.error(request, 'This user is not authorized to edit this post.')
        return render(request, 'post/show.html', {'post': post})

@login_required(login_url='/login/')
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user.id == post.author_id:
        post.delete()
        messages.success(request, 'Successfully deleted.')
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request, 'This user is not authorized to delete this post.')
        return HttpResponseRedirect(reverse('home'))

# ------------------------------------------------------------------------------------- #

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            pass
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return HttpResponseRedirect(reverse('home'))
