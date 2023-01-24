from django.conf import settings
from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MenuCategory(models.Model):
    title = models.CharField(max_length=255)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self):
        return f"{self.menu.title} - {self.title}"


class Dish(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, related_name="items"
    )
    price = models.DecimalField(decimal_places=2, max_digits=10, default=1)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category.title} - {self.title}"

    def get_total_callories(self):
        pass

    def get_minutes_to_cook(self):
        try:
            return self.recipe.minutes_to_cook
        except Dish.recipe.RelatedObjectDoesNotExist:
            return settings.DEFAULT_MINUTES_TO_COOK


class Ingredient(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CalorieItem(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="calorie"
    )
    by_weight = models.DecimalField(decimal_places=3, max_digits=6)


class Recipe(models.Model):    
    dish = models.OneToOneField(
        Dish, on_delete=models.CASCADE, related_name="recipe"
    )
    minutes_to_cook = models.IntegerField(
        default=settings.DEFAULT_MINUTES_TO_COOK
    )

    def __str__(self):
        return self.dish.title


class RecipeIngridient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingridients"
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    weight = models.DecimalField(decimal_places=3, max_digits=6)

    def get_callories(self):
        pass

    def __str__(self):
        return f"{self.ingredient.title} №{self.order_num}"


class RecipeStep(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="steps"
    )
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    order_num = models.IntegerField()

    def __str__(self):
        return f"{self.recipe.title} №{self.order_num}"
