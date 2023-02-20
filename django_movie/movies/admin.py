from django.contrib import admin
from .models import Category, Actor, Rating, RatingStar, Reviews, Genre, MovieShots, Movie

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Movie)
