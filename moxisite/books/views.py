from django.shortcuts import render
from django.http import HttpResponseRedirect
from books.models import Book
from django.core.mail import send_mail
from .forms import ContactForm

def search_form(request):
    return render(request, 'books/search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__incontains=q)
            return render(request, 'books/search_results.html', {'books': books, 'query': q})
    return render(request, 'books/search_form.html', {'error': error})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            f = request.FILES['file']
            des_origin_f = open('/Users/zhongnakakei/Desktop/flower.jpg', "ab")  
            for chunk in f.chunks():  
                des_origin_f.write(chunk)  
            des_origin_f.close()  
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject':'I love u,moxi!'}
        )
    return render(request, 'books/contact_form.html', {'form': form})
