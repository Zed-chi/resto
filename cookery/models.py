from django.db import models


class Dish(models.Model):
    title = models.CharField(max_length=255)

    def get_total_callories(self):
        pass


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name="recipe"
    )


class RecipeStep(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="steps"
    )
    description = models.TextField()
    image = models.ImageField()


class Ingredient(models.Model):
    title = models.CharField(max_length=255)
    weight = models.DecimalField(decimal_places=3, max_digits=6)

    def get_callories(self):
        pass


class CalorieItem(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="calorie"
    )
    by_weight = models.DecimalField(decimal_places=3, max_digits=6)
