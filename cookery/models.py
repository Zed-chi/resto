from django.db import models


class Dish(models.Model):
    title = models.CharField(max_length=255)

    def get_total_callories(self):
        pass

    def __str__(self):
        return self.title


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
    title = models.CharField(max_length=255)
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name="recipe"
    )

    def __str__(self):
        return self.title


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
