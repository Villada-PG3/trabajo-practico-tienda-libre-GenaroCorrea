from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "precio",
        "categoria",
        "activo",
        "fecha",
    )

    list_filter = (
        "categoria",
        "activo",
    )

    search_fields = (
        "nombre",
    )

    list_editable = (
        "precio",
        "activo",
    )