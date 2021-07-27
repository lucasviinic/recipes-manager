from django.contrib import admin
from .models import Recipe

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_da_receita', 'categoria', 'tempo_preparo')
    list_display_links = ('id', 'nome_da_receita')
    search_fields = ('nome_da_receita',)
    list_filter = ('categoria',)
    list_per_page = 5

admin.site.register(Recipe, ListandoReceitas)