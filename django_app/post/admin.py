from django.contrib import admin

from post.models import Post, PostPhoto, PostComment

admin.site.register(Post)
admin.site.register(PostPhoto)
admin.site.register(PostComment)