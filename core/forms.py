from django import forms 
from core.models import Restaurant, Rating
from django.core.validators import MinValueValidator, MaxValueValidator

# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating 
#         fields = ('restaurant', 'user', 'rating')


class RatingForm(forms.Form):
    rating = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Enter a rating between 1 and 10"
    )

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'restaurant_type',)