from django.shortcuts import render
from .forms import RatingForm, RestaurantForm
from .models import Restaurant, Rating, Sale, StaffRestaurant
from django.db.models import Sum, Prefetch
from django.utils import timezone
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

    # restaurants = Restaurant.objects.filter(name__startswith='C').prefetch_related('ratings', 'sales')
    # SELECT * FROM core_restaurant WHERE name LIKE 'C%';
    # SELECT * FROM core_rating WHERE restaurant_id IN (1, 2, 3, ...);
    # SELECT * FROM core_sale WHERE restaurant_id IN (1, 2, 3, ...);

    # restaurants = Restaurant.objects.prefetch_related('ratings', 'sales').filter(ratings__rating=5)
    # SELECT * FROM core_restaurant INNER JOIN core_rating ON core_restaurant.id = core_rating.restaurant_id WHERE core_rating.rating = 5;
    # SELECT * FROM core_rating WHERE restaurant_id IN (1, 2, 3, ...);
    # SELECT * FROM core_sale WHERE restaurant_id IN (1, 2, 3, ...);
    
    # restaurants = Restaurant.objects.prefetch_related('ratings', 'sales').filter(ratings__rating=5).annotate(total=Sum('sales__income'))
    # SELECT core_restaurant.*, SUM(core_sale.income) as total FROM core_restaurant 
    # INNER JOIN core_rating ON core_restaurant.id = core_rating.restaurant_id 
    # LEFT OUTER JOIN core_sale ON core_restaurant.id = core_sale.restaurant_id 
    # WHERE core_rating.rating = 5 
    # GROUP BY core_restaurant.id;

    # month_ago = timezone.now() - timezone.timedelta(days=30)
    # month_sales = Prefetch('sales', queryset=Sale.objects.filter(datetime__gte=month_ago)) # Custom prefetch to get only sales from the last month
    # restaurants = Restaurant.objects.prefetch_related('ratings', month_sales).filter(ratings__rating=5)
    # restaurants = restaurants.annotate(total=Sum('sales__income'))
    # print([r.total for r in restaurants])

    # SELECT core_restaurant.* FROM core_restaurant 
    # INNER JOIN core_rating ON core_restaurant.id = core_rating.restaurant_id 
    # WHERE core_rating.rating = 5;
    # SELECT * FROM core_sale WHERE restaurant_id IN (1, 2, 3, ...) AND datetime >= '2025-10-13 16:49:58.603842+00:00';

    jobs = StaffRestaurant.objects.prefetch_related('staff', 'restaurant')
    for job in jobs:
        print(f"{job.staff.name} works at {job.restaurant.name} with salary {job.salary}")

    # context = {
    #     'restaurants': restaurants,
    # }
    return render(request, 'core/restaurant_index.html')

def rating_index(request):
    # ratings = Rating.objects.select_related('restaurant') # Fetch all ratings with their associated restaurant in optimized query (One to Many relationship)
    # SELECT * FROM core_rating INNER JOIN core_restaurant ON core_rating.restaurant_id = core_restaurant.id;

    ratings = Rating.objects.only('rating', 'restaurant__name').select_related('restaurant')  # Fetch only rating and restaurant name fields
    # SELECT core_rating.rating, core_restaurant.name FROM core_rating INNER JOIN core_restaurant ON core_rating.restaurant_id = core_restaurant.id;

    return render(request, 'core/rating_index.html', {'ratings': ratings})