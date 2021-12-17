from django.contrib import admin

# Register your models here.

from .models import Post, PostView, Like, DisLike, Comment

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(DisLike)
admin.site.register(Comment)