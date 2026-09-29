from django.contrib.auth.models import User

from rest_framework import serializers
from cinema.models import Category, Movie, Subscription, SubscriptionType, UserSubscription

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    type = SubscriptionTypeSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Subscription
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class UserSubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserSubscription
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Movie
        fields = "__all__"
