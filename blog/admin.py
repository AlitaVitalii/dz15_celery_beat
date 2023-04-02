from django.contrib import admin

from blog.models import Author, Quote
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'about')
    search_fields = ['name']
    list_per_page = 10


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'author')
    search_fields = ['quote', 'author']
    list_per_page = 10
