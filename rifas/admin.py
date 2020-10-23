from django.contrib import admin
from .models import skin
from .models import rifa

class Listandoskin(admin.ModelAdmin):
    list_display = ('id', 'nome',)

admin.site.register(skin, Listandoskin)

class Listandorifa(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(rifa, Listandorifa)
