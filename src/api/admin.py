from django.contrib import admin

from api.models import Ingredient, Pizza, PizzaIngredient

admin.site.register(Pizza)
admin.site.register(Ingredient)
admin.site.register(PizzaIngredient)
