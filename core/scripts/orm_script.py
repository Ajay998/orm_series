from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
def run():

    # restaurant = Restaurant()
    # restaurant.name = "My Italian Restaurant"
    # restaurant.latitude = 40.7128
    # restaurant.longitude = -74.0060
    # restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    # restaurant.date_opened = timezone.now().date()
    # restaurant.website = "https://myitalianrestaurant.example.com"
    # restaurant.save()

    # Restaurant.objects.create(
    #     name = "My Chinese Restaurant",
    #     latitude = 34.0522,
    #     longitude = -118.2437,
    #     restaurant_type = Restaurant.TypeChoices.CHINESE,
    #     date_opened = timezone.now().date(),
    #     website = "https://mychineserestaurant.example.com"
    # )

    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 2500.75,
    #     datetime = timezone.now()
    # )

    # restaurant = Restaurant.objects.all()
    # print(restaurant)
    # SELECT * FROM core_restaurant;

    # first_row = Restaurant.objects.first()
    # print(first_row)
    # SELECT * FROM core_restaurant ORDER BY core_restaurant.id ASC LIMIT 1;
    
    # last_row = Restaurant.objects.last()
    # print(last_row)
    # SELECT * FROM core_restaurant ORDER BY core_restaurant.id DESC LIMIT 1;

    # get_first_element = Restaurant.objects.all()[0]
    # print(get_first_element)
    # SELECT * FROM core_restaurant LIMIT 1;

    # print(Restaurant.objects.count())
    # SELECT COUNT(*) FROM core_restaurant;

    # restaurant = Restaurant.objects.first()
    # user = User.objects.first()
    # rating = Rating.objects.create(
    #     restaurant=restaurant,
    #     user=user,
    #     rating=10
    # )
    # print(rating)
    # # INSERT INTO core_rating (restaurant_id, user_id, rating) VALUES (1, 1, 5);
    # print(Rating.objects.all())
    # SELECT * FROM core_rating;

    # rating_five = Rating.objects.filter(rating=5)
    # print(rating_five)
    # SELECT * FROM core_rating WHERE rating = 5;

    # rating_greater_that_five = Rating.objects.filter(rating__gt=5)
    # print(rating_greater_that_five)
    # # SELECT * FROM core_rating WHERE rating > 5;

    # rating_between_five_and_eight = Rating.objects.filter(rating__gte=5, rating__lte=8)
    # print(rating_between_five_and_eight)
    # SELECT * FROM core_rating WHERE rating >= 5 AND rating <= 8;

    # rating_not_equal_to_five = Rating.objects.exclude(rating=5)
    # print(rating_not_equal_to_five)
    # SELECT * FROM core_rating WHERE rating != 5;

    # restaurant = Restaurant.objects.first()
    # print(restaurant.name)
    # restaurant.name = 'Indian Delight'
    # restaurant.save()
    # print(restaurant.name)
    # UPDATE core_restaurant SET name = 'Indian Delight' WHERE id = 1;

    # restaurant = Restaurant.objects.first()
    # rating = Rating.objects.first()
    # print(rating.restaurant)

    # restaurant = Restaurant.objects.first()
    # # print(restaurant.rating_set.all())
    # print(restaurant.ratings.all()) # Modified line to use related_name from ForeignKey
    # SELECT * FROM core_rating WHERE restaurant_id = 1;

    # restaurant = Restaurant.objects.first()
    # print(restaurant.sales.all())  # Using related_name from ForeignKey
    # SELECT * FROM core_sale WHERE restaurant_id = 1;

    # user = User.objects.first()
    # restaurant = Restaurant.objects.first()
    # rating , created = Rating.objects.get_or_create(
    #     restaurant=restaurant,
    #     user=user,
    #     rating=8
    # )
    # print(rating, created) # True if created, False if already existed
    # # SELECT * FROM core_rating WHERE restaurant_id = 1 AND user_id = 1 AND rating = 8;
    # # If not found, then:
    # # INSERT INTO core_rating (restaurant_id, user_id, rating) VALUES (1, 1, 8);

    print(connection.queries)
    