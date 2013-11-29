from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

from blog.models import Blog, UserProfile


from .forms import BlogForm

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES.get("image", None)
            cd = form.cleaned_data
            author = request.user.get_profile()
            blog = Blog(title=cd['title'], body_text=cd['body_text'], image=image, author=author, status=cd['status'], privacy=cd['privacy'])
            blog.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        author = request.user.get_profile()
        print author
        form = BlogForm()
    return render(request, 'blog/show_entries.html', {'form':form})


# def add_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user.save 
#             user = auth.authenticate(username=cd['username'], password=cd['password'], email=cd['email'])
#             auth.login(request, user)
#             return HttpResponseRedirect(reverse('home'))
#     else:
#         form = BlogForm()
#     return render(request, 'blog/register.html', {'form':form})
    

def thank(request):
    return render(request, 'blog/thank.html')

def show_entries(request):
    entry_list = Blog.objects.order_by("-id")
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

def show_wishes(request):
    user_id=request.user.id
    if user_id:
        user = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(user=user)
        entry_list = Blog.objects.filter(author=user_profile).order_by("-id")
    else:
        entry_list = Blog.objects.order_by("-id")

    return render(request, 'blog/show_wishes.html', {"entries": entry_list})

def user_wishes(request, user_id):
    user = User.objects.get(id=user_id)
    user_profile = UserProfile.objects.get(user=user)
    entry_list = Blog.objects.filter(author=user_profile).order_by("-id")
    return render(request, 'blog/show_wishes.html', {"entries": entry_list})

def entry(request, entry_id):
    entry = Blog.objects.get(id=entry_id)
    return render(request, 'blog/entry.html', {'entry': entry})

def wish(request, entry_id):
    entry = Blog.objects.get(id=entry_id)
    return render(request, 'blog/wish.html', {'entry': entry})

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
    return HttpResponseRedirect('/thank/')

@login_required
def edit_entry(request, entry_id):
    entry = Blog.objects.get(id=entry_id)
    if request.method == 'POST':
        #blog = Blog.objects.filter(id=entry_id).update(title=request.POST['title'], body_text=request.POST['body_text'])
        entry.title = request.POST['title']
        entry.body_text = request.POST['body_text']
        entry.save()
        #return HttpResponseRedirect('/entry/', {'entry_id': entry_id})
        return HttpResponseRedirect('/show_entries/')
    return render(request, 'blog/edit_entry.html', {'entry': entry})

@login_required
def delete_entry(request, entry_id):
    entry = Blog.objects.get(id=entry_id)
    entry.delete()
    return HttpResponseRedirect('/show_entries/')
