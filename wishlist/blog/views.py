# coding: utf-8

import os

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

from blog.models import Blog, UserProfile


from .forms import BlogForm, UserForm

@login_required
def add_entry(request):
    if request.method == 'POST':
            author = request.user.get_profile()
            wish = Blog(author=author)
            blog=BlogForm(request.POST, request.FILES, instance=wish)
            blog = blog.save()
            if blog.image:
                path = blog.image.path.encode('utf-8')
                os.system("gm convert {path} -thumbnail '630x460^' -gravity center -extent 630x460 {path}".format(path=path))
            return HttpResponseRedirect(reverse('home'))
    else:
        form = BlogForm()
        return render(request, 'blog/show_entries.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  
            user = User.objects.create_user(username=cd['username'], password=cd['password'], email=cd['email'])
            user.save
            user = auth.authenticate(username=cd['username'], password=cd['password'], email=cd['email'])
            auth.login(request, user)
            return HttpResponseRedirect('/show_wishes/')
    else:
        form = UserForm()
    return render(request, 'blog/register.html', {'form':form})
    
@login_required
def show_entries(request):
    entry_list = Blog.objects.exclude(privacy="Yes").order_by("-id")
    paginator = Paginator(entry_list, 5)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        entries = paginator.page(page)
    except (EmptyPage, InvalidPage):
        entries = paginator.page(paginator.num_pages)

    form = BlogForm()
    return render(request, 'blog/show_entries.html', {"entries": entries, 'form': form})

def all_wishes(request):
    entry_list = Blog.objects.exclude(privacy="Yes").order_by("-id")
    return render(request, 'blog/show_wishes.html', {"entries": entry_list})

def show_wishes(request):
    user_id=request.user.id
    if user_id:
        user = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(user=user)
        entry_list = Blog.objects.filter(author=user_profile).order_by("-id")
    else:
        entry_list = Blog.objects.exclude(privacy="Yes").order_by("-id")

    return render(request, 'blog/show_wishes.html', {"entries": entry_list})

def user_wishes(request, user_id):
    user = User.objects.get(id=user_id)
    user_profile = UserProfile.objects.get(user=user)
    entry_list = Blog.objects.filter(author=user_profile).order_by("-id")
    return render(request, 'blog/show_wishes.html', {"entries": entry_list, "title":user.username})

def entry(request, entry_id):
    entry = Blog.objects.get(id=entry_id)
    return render(request, 'blog/entry.html', {'entry': entry})

def wish(request, wish_id):
    wish = Blog.objects.get(id=wish_id)
    if request.user.is_authenticated():
        login_user = request.user.get_profile().user.username
    else:
        login_user = ""
    return render(request, 'blog/wish.html', {'wish': wish, 'login_user': login_user})

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required
def edit_wish(request, wish_id):
    wish = Blog.objects.get(id=wish_id)
    if wish.author == request.user.get_profile() and request.method == 'POST':
        blog = BlogForm(request.POST, request.FILES, instance=wish)
        blog = blog.save()
        if blog.image:
            path = blog.image.path.encode('utf-8')
            os.system("gm convert {path} -thumbnail '630x460^' -gravity center -extent 630x460 {path}".format(path=path))
        return HttpResponseRedirect(reverse('home'))
    else:
        form = BlogForm(instance=wish)
        return render(request, 'blog/edit_wish.html', {'form': form})

def about(request):
    return render(request, 'blog/about.html')

def search(request):
  name = request.POST.get('search',None)
  return HttpResponseRedirect('/all_wishes/',)


@login_required
def delete_wish(request, wish_id):
    wish = Blog.objects.get(id=wish_id)
    if wish.author == request.user.get_profile():
        wish.delete()
    return HttpResponseRedirect('/')
