from django.contrib import admin
from .models import Book, Author, Address


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'author', 'rating', 'is_bestselling')

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)