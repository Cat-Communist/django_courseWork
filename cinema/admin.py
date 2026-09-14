from django.contrib import admin
from cinema.models import Subscription, SubscriptionType, Movie, Category

# Register your models here.
@admin.register(Subscription)
class SubscribtionAdmin(admin.ModelAdmin):
    list_display=["id", "type", "duration"]

@admin.register(SubscriptionType)
class SubscribtionTypeAdmin(admin.ModelAdmin):
    list_display=["id", "title"]

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=["id", "title", "category", "duration", "rating"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["id", "title"]