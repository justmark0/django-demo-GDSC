from django.db import models


class Flavor(models.TextChoices):
    sweet = "sweet"
    salty = "salty"
    sour = "sour"
    bitter = "bitter"
    umami = "umami"


class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name="ingredient name")
    flavor = models.CharField(
        max_length=10, choices=Flavor.choices, null=True, blank=True
    )


class Pizza(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the pizza")
    ingredients = models.ManyToManyField(Ingredient, through="PizzaIngredient")
    size = models.IntegerField(
        verbose_name="diameter, cm", help_text="diameter of pizza in centimeters"
    )


class PizzaIngredient(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_amount = models.IntegerField(default=1)
