from django.contrib import admin

from .models import Audio, Genre


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    """Audio"""
    list_display = ("id", "name", "audio", "date")
    list_display_links = ("name",)
    list_filter = ("genres", )
    search_fields = ("name", )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")


admin.site.site_title = "Audio Blog"
admin.site.site_header = "Audio Blog"
