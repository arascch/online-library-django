from django.contrib import admin
from .models import Book, BookInstance, Genre , Author

admin.register(Book)
admin.register(Author)
admin.register(Genre)
admin.register(BookInstance)
# Register your models here.
