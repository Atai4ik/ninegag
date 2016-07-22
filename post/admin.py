from django.contrib import admin
from post.models import Post, Categories


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    model = Post

admin.site.register(Post, ArticleAdmin)
admin.site.register(Categories)
