from django.contrib import admin

from .models import Comment, Notice, Newsletter

admin.site.register(Notice)
admin.site.register(Newsletter)
admin.site.register(Comment)
