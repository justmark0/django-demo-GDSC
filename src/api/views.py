import logging

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import mixins, permissions, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.models import Ingredient, Pizza
from api.serializers.ingredient import IngredientWriteSerializer
from api.serializers.pizza import PizzaReadSerializer, PizzaWriteSerializer
from api.serializers.pizza_ingredient import (
    PizzaIngredientForPizzaReadSerializer,
    PizzaIngredientWriteSerializer,
)
from api.serializers.user import UserLoginSerializer

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    serializer_class = UserLoginSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.data["username"], password=serializer.data["password"]
        )
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class PizzaViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Pizza.objects.all()

    def get_serializer_class(self):
        """Return serializer depending on action"""
        if self.action in (
            "list",
            "retrieve",
        ):
            return PizzaReadSerializer
        elif self.action in (
            "create",
            "update",
            "partial_update",
        ):
            return PizzaWriteSerializer
        return None


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientWriteSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class PizzaIngredientViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Ingredient.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        """Return serializer depending on action"""
        return PizzaIngredientWriteSerializer
