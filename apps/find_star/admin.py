from django.contrib import admin
from apps.find_star.models import Birth, Image, Post


@admin.register(Birth)
class BirthAdmin(admin.ModelAdmin):
    list_display = ["id", "birth", "word"]
    search_fields = ["birth", "word"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["id", "birth", "url"]
    search_fields = ["birth__birth", "url"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "birth", "post"]
    search_fields = ["birth__birth"]
