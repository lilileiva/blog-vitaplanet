from django.contrib import admin

# Register your models here.

from .models import Post, PostView, DisLike, Comment, Category

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Category)
admin.site.register(DisLike)
admin.site.register(Comment)