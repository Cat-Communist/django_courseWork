from rest_framework import serializers
from cinema.models import Movie, Subscription, SubscriptionType

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = "__all__"

        
class SubscriptionSerializer(serializers.ModelSerializer):
    type = SubscriptionTypeSerializer(read_only=True)
    
    class Meta:
        model = Subscription
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "duration"]