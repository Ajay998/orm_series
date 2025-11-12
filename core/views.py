from django.shortcuts import render
from .forms import RatingForm, RestaurantForm
from .models import Restaurant
# Create your views here.

def submit_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
            return render(request, 'core/rating_submitted.html')
        else:
            return render(request, 'core/rating_submitted.html', {'form': form})
    else:
        form = RatingForm()
    return render(request, 'core/rating_submitted.html', {'form': form})

def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'core/restaurant_created.html')
        else:
            return render(request, 'core/restaurant_created.html', {'form': form})
    else:
        form = RestaurantForm()
    return render(request, 'core/restaurant_created.html', {'form': form})

def index(request):
    restaurant = Restaurant.objects.all()
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'core/index.html', context)