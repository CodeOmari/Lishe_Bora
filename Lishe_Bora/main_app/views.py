from django.contrib.auth.models import User
from .serializers import CustomUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import IngredientSerializer, RecipeSerializer
from .models import Recipe, Ingredient
from rest_framework import viewsets, permissions

# Create your views here.
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

# Ensures only the author of a recipe can update/delete it   
class IsRecipeAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
    


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated, IsRecipeAuthorOrReadOnly]

    # Sets the currently logged in user as the owner of the event they created
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # authors can only see recipes they own
    # Other users can see all recipes
    def get_queryset(self):
        user= self.request.user
        if Recipe.objects.filter(author=user).exists():
            return Recipe.objects.filter(author=user)
        return Recipe.objects.all()
    

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]