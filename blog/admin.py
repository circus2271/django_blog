from django.contrib import admin
from .models import Post, Comment, Choice

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    search_fields = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Choice)
