from os import name
from myapp.models import Book
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import Book
from .forms import Bookform,forms

# Create your views here.

def index(requests):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }
    return render(requests,'myapp/index.html',context)


def detail(requests,book_id):
    book = Book.objects.get(id = book_id)
    return render(requests,'myapp/details.html',{'book':book})

def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        book_image = request.FILES['book_image']
        
        book = Book(name=name, desc=desc, price=price,book_image=book_image)
        book.save()
    return render(request,'myapp/add_book.html')


def update(request, id):
    book = Book.objects.get(id = id)
    form = Bookform(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/edit.html',{'form':form, 'book':book})


def delete(request, id):
    if request.method=="POST":
        book = Book.objects.get(id = id)
        book.delete()
    return render(request,'myapp/delete.html')