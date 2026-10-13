"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cinema import views

from rest_framework.routers import DefaultRouter
from cinema.api import Category2MovieViewset, CategoryViewset, MovieViewset, Sub2CatViewset, Subscription2UserViewset, SubscriptionViewset, UserProfileViewset

router = DefaultRouter()
router.register("movies", MovieViewset, basename="movies")
router.register("movie-categories", Category2MovieViewset, basename="movie-categories")
router.register("user-profiles", UserProfileViewset, basename="user-profiles")
router.register("subscriptions", SubscriptionViewset, basename="subscriptions")
router.register("user-subscriptions", Subscription2UserViewset, basename="user-subscriptions")
router.register("subscription-categories", Sub2CatViewset, basename="subscription-types")
router.register("categories", CategoryViewset, basename="categories")

urlpatterns = [
    path('view-test/', views.ShowMoviesView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
