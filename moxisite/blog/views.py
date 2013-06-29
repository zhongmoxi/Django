from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from blog.models import Blog

def add_entry(request):
    if request.method == 'POST':
        blog = Blog.objects.create(title=request.POST['title'], body_text=request.POST['body_text'])
        blog.save()
        return HttpResponseRedirect('/thank/')
        #return render(request, 'blog/thank.html')

        #blog = BlogForm(request.POST)
        #if form.is_valid():
        #    blog = form.save()
        #    return render(request, 'blog/show_entries.html')
    #else:
    #    form = BlogForm()
    return render(request, 'blog/show_entries.html')

def thank(request):
    return render(request,'blog/thank.html')

def show_entries(request):
    entries = Blog.objects.all()
    return render(request, 'blog/show_entries.html', {'entries':entries})

def entry(request, entry_id):
    entry = Blog.objects.get(id=entry_id)
    return render(request, 'blog/entry.html', {'entry': entry})
