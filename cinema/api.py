from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from cinema.models import Movie, Subscription
from cinema.serializers import MovieSerializer, SubscriptionSerializer

class MovieViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SubscriptionViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
