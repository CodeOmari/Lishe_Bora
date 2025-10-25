from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    instructions = models.TextField()
    duration = models.IntegerField(help_text='Duration in minutes', 
                                   verbose_name='Preparation Duration(min)')
    serving = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.title}'
    
    class Meta:
        db_table = 'Recipe'
        ordering = ['title']


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.recipe.title}'
    
    class Meta:
        db_table = 'Ingredient'
        ordering = ['recipe']