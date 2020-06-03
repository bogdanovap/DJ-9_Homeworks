from django.shortcuts import render

from books.models import Book
from django.core.paginator import Paginator
import datetime


def books_view(request, date: datetime.date = None):
    
    book_list = Book.objects.all()
    prev_date = datetime.date 
    next_date = datetime.date
    if date != None:
        next_book = book_list.filter(pub_date__gt=date).order_by('pub_date').first()
        next_date = next_book.pub_date if next_book else None
        prev_book = book_list.filter(pub_date__lt=date).order_by('-pub_date').first()
        prev_date = prev_book.pub_date if prev_book else None
        book_list = book_list.filter(pub_date=date)  

    template = 'books/books_list.html'
    context = {'books': book_list, 'prev_date':prev_date, 'next_date':next_date}
    return render(request, template, context)
