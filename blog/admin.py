from django.contrib import admin
from .models import blogposts
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    pass
admin.site.register(blogposts , BlogAdmin)