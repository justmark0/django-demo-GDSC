from rest_framework import serializers

from api.models import PizzaIngredient
from api.serializers.ingredient import IngredientReadSerializer


class PizzaIngredientForPizzaReadSerializer(serializers.ModelSerializer):
    ingredient = IngredientReadSerializer(read_only=True)

    class Meta:
        model = PizzaIngredient
        fields = [
            "id",
            "ingredient",
            "ingredient_amount",
        ]
        read_only_fields = fields
        prefetch_related = ("ingredient",)


class PizzaIngredientWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaIngredient
        fields = [
            "id",
            "pizza",
            "ingredient",
            "ingredient_amount",
        ]

    def validate(self, attrs):
        return attrs
