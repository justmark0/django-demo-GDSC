from rest_framework.routers import DefaultRouter

from api.views import (
    IngredientViewSet,
    PizzaIngredientViewSet,
    PizzaViewSet,
    UserViewSet,
)

router = DefaultRouter()

router.register("pizza", PizzaViewSet, "pizza")
router.register("ingredient", IngredientViewSet, "ingredient")
router.register("pizza-ingredient", PizzaIngredientViewSet, "pizza_ingredient")
router.register("user", UserViewSet, "user")

urlpatterns = []
urlpatterns.extend(router.urls)
