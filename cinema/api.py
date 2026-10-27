from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from cinema.models import Category, Category2Movie, Movie, Subscription, Subscription2Category, Subscription2User, UserProfile
from cinema.serializers import Category2MovieSerializer, CategorySerializer, MovieSerializer, Sub2CatSerializer, Subscription2UserSerializer, SubscriptionSerializer, UserProfileSerializer

class Subscription2UserViewset(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = Subscription2User.objects.all()
    serializer_class = Subscription2UserSerializer

class MovieViewset(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class Category2MovieViewset(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = Category2Movie.objects.all()
    serializer_class = Category2MovieSerializer

class Sub2CatViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = Subscription2Category.objects.all()
    serializer_class = Sub2CatSerializer

class CategoryViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin, 
    GenericViewSet
):
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


class UserProfileViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer