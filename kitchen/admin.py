from django.contrib import admin

from .models import (CalorieItem, Dish, Ingredient, Menu, MenuCategory, Recipe,
                     RecipeStep, RecipeIngridient)


admin.site.register(Dish)
admin.site.register(CalorieItem)
admin.site.register(Ingredient)


admin.site.register(RecipeStep)
class RecipeStepInline(admin.TabularInline):
    model = RecipeStep


class RecipeIngridientInline(admin.TabularInline):
    model = RecipeIngridient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeStepInline,RecipeIngridientInline]


class MenuCategoryInline(admin.StackedInline):
    model = MenuCategory


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuCategoryInline,]



class DishInline(admin.StackedInline):
    model = Dish


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    inlines = [DishInline,]
