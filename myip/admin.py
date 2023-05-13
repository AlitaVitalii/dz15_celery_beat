from django.contrib import admin

from myip.models import Myip

# Register your models here.

# admin.site.register(Myip)


@admin.register(Myip)
class MyipAdmin(admin.ModelAdmin):
    list_display = ('pubdate', 'ip_txt')
    # fields = ('pubdate', 'ip_txt')
    list_filter = ['pubdate']
    # date_hierarchy = ['pubdate']
    list_per_page = 20
