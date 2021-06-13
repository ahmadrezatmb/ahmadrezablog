from django.contrib import admin
from .models import favmovie,favmusic,skills
# Register your models here.
class favoritemusic(admin.ModelAdmin):
    pass
admin.site.register(favmusic , favoritemusic)

class favoritemovie(admin.ModelAdmin):
    pass
admin.site.register(favmovie , favoritemovie)

class sk(admin.ModelAdmin):
    pass
admin.site.register(skills , sk)