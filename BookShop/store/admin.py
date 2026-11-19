from django.contrib import admin

# Register your models here.

from .models import Category, Author, Book,AuthorProfile
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(AuthorProfile)
