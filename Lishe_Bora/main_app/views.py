from django.shortcuts import render

from django.contrib.auth.models import User
from .serializers import CustomUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import IngredientSerializer, RecipeSerializer
from .models import Recipe, Ingredient
from rest_framework import viewsets

# Create your views here.
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]