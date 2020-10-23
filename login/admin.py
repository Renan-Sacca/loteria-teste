from django.contrib import admin
from .models import Pessoa
from .models import Profile

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 2

admin.site.register(Pessoa, ListandoPessoas)

class Listandoprofiles(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id','user',)

admin.site.register(Profile, Listandoprofiles)
