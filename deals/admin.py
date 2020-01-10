from django.contrib import admin
from .models import Deal, Category, Brand, Shop


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    readonly_fields = ['slug']
    search_fields = ['name']
    list_filter = []


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    readonly_fields = ['slug']
    search_fields = ['name']
    list_filter = []


@admin.register(Brand)
class CategoryGroupAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    readonly_fields = ['slug']
    search_fields = ['name']


@admin.register(Shop)
class CategoryGroupAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    readonly_fields = ['slug']
    search_fields = ['name']