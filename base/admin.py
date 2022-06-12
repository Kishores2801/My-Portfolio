from django.contrib import admin

# Register your models here.

from .models import Project, Blog, Tag



admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Tag)
