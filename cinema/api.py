from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from cinema.models import Category, Movie, Subscription, SubscriptionType, UserSubscription
from cinema.serializers import CategorySerializer, MovieSerializer, SubscriptionSerializer, SubscriptionTypeSerializer, UserSubscriptionSerializer

class UserSubscriptionViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

class MovieViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SubscriptionTypeViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = SubscriptionType.objects.all()
    serializer_class = SubscriptionTypeSerializer

class CategoryViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubscriptionViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
