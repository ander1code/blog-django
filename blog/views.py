#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.models import User

# Authentication:
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from datetime import datetime
from django.urls import reverse

def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Successfully logged.')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Invalid Username and Password.')
            return render(request, 'login.html', {'statuslog': 2})
    else:
        return render(request, 'login.html', {'statuslog': 2})

def home(request):
    if request.POST:
        p_search = request.POST['search'] + '%'
        posts = Post.objects.extra(where=["title LIKE %s"], params=[p_search]).order_by('-createDate')
        if len(posts) == 0:
            messages.warning(
                request, 'No articles were found with these titles.')
        paginator = Paginator(posts, 7)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        postsAll = Post.objects.all().order_by('-createDate')
        postLast = postsAll[:1]
        post2 = postsAll[1:5]
        post3 = postsAll[5:8]
        return render(request, 'home.html', {'postsAll': postsAll, 'postLast': postLast, 'post2': post2, 'post3': post3})
    else:
        postsAll = Post.objects.all().order_by('-createDate')
        postLast = postsAll[:1]
        post2 = postsAll[1:5]
        post3 = postsAll[5:8]

        paginator = Paginator(postsAll, 7)
        page = request.GET.get('page')
        try:
            postsAll = paginator.page(page)
        except PageNotAnInteger:
            postsAll = paginator.page(1)
        except EmptyPage:
            postsAll = paginator.page(paginator.num_pages)
        return render(request, 'home.html', {'postsAll': postsAll, 'postLast': postLast, 'post2': post2, 'post3': post3})

@login_required(login_url="/login/")
def create(request):
    if request.method == 'POST':
        frm = frmPost(request.POST, request.FILES)
        if frm.is_valid():
            post = frm.save(commit=False)
            post.author = request.user
            post.title = frm.cleaned_data.get('title')
            post.briefing = frm.cleaned_data.get('briefing')
            post.text = frm.cleaned_data.get('text')
            post.image = frm.cleaned_data.get('image')
            post.createDate = datetime.now()
            post.updateDate = None
            post.save()
            messages.success(request, 'Successfully created.')
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'create.html', {'form': frm})
    else:
        frm = frmPost(initial={'title': '', 'briefing': '', 'text': ''})
    return render(request, 'create.html', {'form': frm})

def show(request, id):
    post = get_object_or_404(Post, id=id)
    autor = User.objects.get(id=post.author_id)
    return render(request, "show.html", {'post': post, 'author': autor})

@login_required(login_url='/login/')
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    createDate = post.createDate
    if request.user.id == post.author_id:
        if request.method == 'POST':
            frm = frmPost(request.POST, request.FILES, instance=post)
            if frm.is_valid():
                post = frm.save(commit=False)
                post.author_id = request.user.id
                post.title = frm.cleaned_data.get('title')
                post.briefing = frm.cleaned_data.get('briefing')
                post.text = frm.cleaned_data.get('text')
                post.image = frm.cleaned_data.get('image')
                post.createDate = createDate
                post.UpdateDate = datetime.now()
                post.save()
                messages.success(request, 'Successfully edited.')
                return render(request, 'show.html', {'post': post})
            else:
                return render(request, 'edit.html', {'form': frm, 'post_id': id})
        else:
            frm = frmPost(initial={'briefing': post.briefing,
                                   'title': post.title,
                                   'text': post.text,
                                   'image': post.image})

        return render(request, 'edit.html', {'form': frm, 'post_id': id})
    else:
        messages.error(
            request, 'This user is not authorized to edit this post.')
    return render(request, 'show.html', {'post': post})


@login_required(login_url='/login/')
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user.id == post.author_id:
        post.delete()
        messages.success(request, 'Successfully deleted.')
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(
            request, 'This user is not authorized to delete this post.')
        return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
def do_logout(request):
    logout(request)
    messages.success(request, 'Sucessfully logout.')
    return HttpResponseRedirect(reverse('home'))
