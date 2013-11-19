from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from blog.models import Blog
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .forms import BlogForm
# from models import Blog

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            blog = Blog(title=cd['title'], body_text=cd['body_text'])
            blog.save()
            f = request.FILES['img']
            des_origin_f = open('/Users/zhongnakakei/Documents/Django/moxisite/blog/static/img/test.jpg', "ab")
            for chunk in f.chunks():
                des_origin_f.write(chunk)
            des_origin_f.close()
            return HttpResponseRedirect('/show_entries/')
    else:
        form = BlogForm()
    return render(request, 'blog/show_entries.html', {'form':form})

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

    return render(request, 'blog/show_entries.html', {"entries": entries})

def entry(request, entry_id):
    entry = Blog.objects.get(id=entry_id)
    return render(request, 'blog/entry.html', {'entry': entry})

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/show_entries/')
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
