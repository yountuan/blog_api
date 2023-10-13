from django.contrib import admin
from .models import Category, Post
from review.models import Comment


# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category']
#     list_filter = ['title', 'created_at']
#     search_fields = ['title', 'body']


class CommentInLine(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


admin.site.register(Post, PostAdmin)