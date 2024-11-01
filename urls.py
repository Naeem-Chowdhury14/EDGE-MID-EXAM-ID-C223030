from django.urls import path
from . import views

urlpatterns = [
    path('recent-books/', views.recent_books, name='recent_books'),
]
