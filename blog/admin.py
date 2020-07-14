from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



@ admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'image', 'publish', 'body', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    summernote_fields = ('body')


@ admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@ admin.register(Aboutme)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title','image','Body','status')
    summernote_fields = ('Body')

