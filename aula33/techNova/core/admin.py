from django.contrib import admin

# Register your models here.

from django.contrib import admin
from core.models import Produto, CustomUser

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    search_fields = ('nome',)
    list_filter = ('categoria',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'bio')
