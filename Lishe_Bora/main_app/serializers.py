from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Recipe, Ingredient

class CustomUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password1']
        )
        return user


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['recipe', 'name', 'quantity']
        read_only_fields = ['id', 'created_at', 'updated_at']



class RecipeSerializer(serializers.ModelSerializer):
    # ingredients = IngredientSerializer(many=True, read_only=True, source='ingredient_set')

    class Meta:
        model = Recipe
        fields = ['author', 'title', 'description', 'instructions', 'duration', 'serving']
        read_only_fields = ['id', 'created_at', 'updated_at']
