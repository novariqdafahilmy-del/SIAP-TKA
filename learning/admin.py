from django.contrib import admin
from .models import Subject, Material


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "is_published", "created_at")
    list_filter = ("subject", "is_published")
    search_fields = ("title", "description", "content")
    prepopulated_fields = {"slug": ("title",)}
