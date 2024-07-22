from django.db import models

# Create your models here.
class Exercises(models.Model):

    class Category_choices(models.TextChoices):
            BASIC = 'Basic'
            INTERMEDIATE = 'Intermediate'
            ADVANCED = 'Advanced'

    category = models.CharField(choices=Category_choices.choices, max_length=50)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    code = models.TextField()

    def __str__(self):
          return f'{self.title}'
