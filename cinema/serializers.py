from django.contrib.auth.models import User

from rest_framework import serializers
from cinema.models import Category, Category2Movie, Movie, Subscription, Subscription2Category, Subscription2User, UserProfile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Subscription
        fields = "__all__"

class Sub2CatSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Subscription2Category
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Movie
        fields = "__all__"

class Category2MovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer
    category = CategorySerializer
    
    class Meta:
        model = Category2Movie
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer
    
    class Meta:
        model = UserProfile
        fields = "__all__"

class Subscription2UserSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer
    user = UserProfileSerializer

    class Meta:
        model = Subscription2User
        fields = "__all__"