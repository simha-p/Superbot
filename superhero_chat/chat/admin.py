

# Register your models here.
from django.contrib import admin
from .models import Hero

class HeroAdmin(admin.ModelAdmin):
  list_display = ('name', 'image', 'background_image', 'icon')

admin.site.register(Hero, HeroAdmin)