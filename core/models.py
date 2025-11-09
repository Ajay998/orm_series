from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
# Restaurant model

def validate_resaurant_name_begins_with_a(value):
    if not value.lower().startswith('a'):
        raise ValidationError(
            f'Restaurant name must begin with the letter A. "{value}" does not.'
        )

class Restaurant(models.Model):

    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        ITALIAN = 'IT', 'Italian'   
        CHINESE = 'CH', 'Chinese'
        MEXICAN = 'MX', 'Mexican'
        AMERICAN = 'AM', 'American'
        GREEK = 'GR', 'Greek'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=100, validators=[validate_resaurant_name_begins_with_a])
    website = models.URLField(default='', blank=True)
    date_opened = models.DateField()
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    restaurant_type = models.CharField(
        max_length=2,
        choices=TypeChoices.choices,
        default=TypeChoices.OTHER,
    )

    def __str__(self):
        return self.name

# Rating model
class Rating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.rating}"

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.income} on {self.datetime} for {self.restaurant.name}"