from django.shortcuts import render
from .forms import RatingForm, RestaurantForm
from .models import Restaurant, Rating
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
    # restaurants = Restaurant.objects.prefetch_related('ratings', 'sales') # Fetch all restaurants with their ratings and sales in optimized queries
    # SELECT * FROM core_restaurant;
    # SELECT * FROM core_rating WHERE restaurant_id IN (1, 2, 3, ...);
    # SELECT * FROM core_sale WHERE restaurant_id IN (1, 2, 3, ...);

    restaurants = Restaurant.objects.filter(name__startswith='C').prefetch_related('ratings', 'sales')
    # SELECT * FROM core_restaurant WHERE name LIKE 'C%';
    # SELECT * FROM core_rating WHERE restaurant_id IN (1, 2, 3, ...);
    # SELECT * FROM core_sale WHERE restaurant_id IN (1, 2, 3, ...);

    context = {
        'restaurants': restaurants,
    }
    return render(request, 'core/restaurant_index.html', context)

def rating_index(request):
    ratings = Rating.objects.select_related('restaurant') # Fetch all ratings with their associated restaurant in optimized query (One to Many relationship)
    # SELECT * FROM core_rating INNER JOIN core_restaurant ON core_rating.restaurant_id = core_restaurant.id;
    return render(request, 'core/rating_index.html', {'ratings': ratings})