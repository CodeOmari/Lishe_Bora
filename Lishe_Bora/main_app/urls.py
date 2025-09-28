from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, IngredientViewSet


router = DefaultRouter()
router.register(r'recipe', RecipeViewSet, basename='recipe') # api/recipe
router.register(r'ingredient', IngredientViewSet, basename='ingredient') # api/ingredient

urlpatterns = [
    path('', include(router.urls)),
]