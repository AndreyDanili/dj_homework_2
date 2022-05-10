from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_info = Book.objects.all()
    context = {
        'books': books_info
    }
    return render(request, template, context)


def books_pub_date(request, pub_date):
    template = 'books/book_info.html'
    back_book = Book.objects.filter(pub_date__lt=pub_date)

    order_back_book = back_book.order_by('-pub_date')
    if len(order_back_book) == 0:
        order_back_book = ['']

    next_book = Book.objects.filter(pub_date__gt=pub_date)
    order_next_book = next_book.order_by('pub_date')
    if len(order_next_book) == 0:
        order_next_book = ['']

    book_info = Book.objects.filter(pub_date=pub_date)
    context = {
        'books': book_info,
        'back_page': order_back_book[0],
        'next_page': order_next_book[0],
    }
    return render(request, template, context)
