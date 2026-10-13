from django.contrib import admin
from cinema.models import Category2Movie, Subscription, Movie, Category, Subscription2Category, Subscription2User, UserProfile

# Register your models here.
@admin.register(Subscription)
class SubscribtionAdmin(admin.ModelAdmin):
    list_display=["id", "title", "price", "duration"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["id", "title"]

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=["id", "title", "duration", "description"]

@admin.register(Category2Movie)
class Category2MovieAdmin(admin.ModelAdmin):
    list_display=["id", "movie", "category"]

@admin.register(Subscription2Category)
class Subscription2CategoryAdmin(admin.ModelAdmin):
    list_display=["id", "subscription", "category"]

@admin.register(Subscription2User)
class Subscription2UserAdmin(admin.ModelAdmin):
    list_display=["id", "user", "subscription", "date_subscription"]

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=["id", "user", "role", "account_money"]