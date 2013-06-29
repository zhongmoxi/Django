from django.contrib import admin
from blog.models import Blog, User

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_text')
    search_fields = ('title', 'body_text')


class BlogUser(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username', 'password')

admin.site.register(Blog)
admin.site.register(User)
