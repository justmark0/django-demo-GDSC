from rest_framework import serializers

from api.models import Pizza
from api.serializers.pizza_ingredient import PizzaIngredientForPizzaReadSerializer


class PizzaReadSerializer(serializers.ModelSerializer):
    ingredients = PizzaIngredientForPizzaReadSerializer(many=True, read_only=True)

    class Meta:
        model = Pizza
        fields = [
            "id",
            "name",
            "ingredients",
            "size",
        ]
        read_only_fields = fields
        prefetch_related = [
            "ingredients",
        ]


class PizzaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = [
            "id",
            "name",
            "size",
        ]
