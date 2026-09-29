from django.contrib import admin
from cinema.models import Subscription, SubscriptionType, Movie, Category, UserSubscription

# Register your models here.
@admin.register(Subscription)
class SubscribtionAdmin(admin.ModelAdmin):
    list_display=["id", "type", "category", "price"]

@admin.register(SubscriptionType)
class SubscribtionTypeAdmin(admin.ModelAdmin):
    list_display=["id", "title", "duration"]

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=["id", "title", "category", "duration", "description"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["id", "title"]

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display=["id", "user", "subscription", "last_payment", "is_active"]