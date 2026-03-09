from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Appetizers)
class AppetizersAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )

@admin.register(models.Salads)
class SaladsAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )

@admin.register(models.Soups)
class SoupsAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )

@admin.register(models.Pasta)
class PastaAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )

@admin.register(models.Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )

@admin.register(models.Seafood)
class SeafoodAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )

@admin.register(models.Steaks)
class SteaksAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )

@admin.register(models.Burgers)
class BurgersAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Sandwiches)
class SandwichesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Vegetarian)
class VegetarianAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Vegan)
class VeganAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.GlutenFree)
class GlutenFreeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Desserts)
class DessertsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Beverages)
class BeveragesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Cocktails)
class CocktailsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Breakfast)
class BreakfastAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Brunch)
class BrunchAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.KidsMenu)
class KidsMenuAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Sides)
class SidesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )


@admin.register(models.Specials)
class SpecialsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'image_url'
    )