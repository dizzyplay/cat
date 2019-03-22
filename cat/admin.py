from django.contrib import admin
from .models import Cat, Meal, CatStatus


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Meal)
class MealsAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CatStatus)
class MealsAdmin(admin.ModelAdmin):
    list_display = ['title']
