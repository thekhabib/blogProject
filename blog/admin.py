from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_time']
    list_filter = ['author', 'created_time']
    search_fields = ['title']
    date_hierarchy = 'created_time'

    class Meta:
        ordering = ('-created_time',)
