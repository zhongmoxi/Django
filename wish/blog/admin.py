from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_text')
    search_fields = ('title', 'body_text')


admin.site.register(Blog)
