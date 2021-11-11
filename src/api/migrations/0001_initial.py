# Generated by Django 3.2.9 on 2021-11-11 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="ingredient name"),
                ),
                (
                    "flavor",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("sweet", "Sweet"),
                            ("salty", "Salty"),
                            ("sour", "Sour"),
                            ("bitter", "Bitter"),
                            ("umami", "Umami"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pizza",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Name of the Team",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "size",
                    models.IntegerField(
                        help_text="diameter of pizza in centimeters",
                        verbose_name="diameter, cm",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PizzaIngredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ingredient_amount", models.IntegerField(default=1)),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.ingredient"
                    ),
                ),
                (
                    "pizza",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.pizza"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pizza",
            name="ingredients",
            field=models.ManyToManyField(
                through="api.PizzaIngredient", to="api.Ingredient"
            ),
        ),
    ]
