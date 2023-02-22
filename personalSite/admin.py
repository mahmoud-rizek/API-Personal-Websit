from django.contrib import admin
from .models import post, project, info, comment
# Register your models here.

admin.site.register(post)
admin.site.register(project)
admin.site.register(info)
admin.site.register(comment)