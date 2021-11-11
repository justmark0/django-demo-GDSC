from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Flavor, Ingredient


class IngredientReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            "id",
            "name",
            "flavor",
        ]
        read_only_fields = fields


class IngredientWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            "id",
            "name",
            "flavor",
        ]

    def validate_flavor(self, flavor):
        if flavor not in Flavor.choices:
            raise ValidationError(
                f"No such flavor. You can use only {list(Flavor.choices)}"
            )
