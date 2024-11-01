from django.shortcuts import render
from django.utils import timezone
from .models import Book

def recent_books(request):
    current_year = timezone.now().year
    five_years_ago = current_year - 5
    recent_books = Book.objects.filter(publication_year__gte=five_years_ago)
    return render(request, 'recent_books.html', {'books': recent_books})
