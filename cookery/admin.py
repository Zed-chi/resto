from django.contrib import admin

from .models import CalorieItem, Dish, Ingredient, Recipe, RecipeStep

admin.site.register(Recipe)
admin.site.register(Dish)
admin.site.register(RecipeStep)
admin.site.register(Ingredient)
admin.site.register(CalorieItem)
