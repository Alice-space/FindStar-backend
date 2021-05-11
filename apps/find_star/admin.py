from django.contrib import admin
from apps.find_star.models import Birth, Image


@admin.register(Birth)
class Birth(admin.ModelAdmin):
    list_display = ["id", "birth"]
    search_fields = ["birth"]


@admin.register(Image)
class Image(admin.ModelAdmin):
    list_display = ["id", "birth", "url"]
    search_fields = ["birth__birth", "url"]
