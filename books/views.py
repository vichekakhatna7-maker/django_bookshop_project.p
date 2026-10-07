from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# បង្កើត list និងបន្ថែមសៀវភៅថ្មី (GET, POST)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# មើលលម្អិត កែប្រែ ឬលុបសៀវភៅ (GET, PUT, DELETE)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer