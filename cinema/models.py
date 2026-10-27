from django.utils import timezone

from django.db import models

# Create your models here.

# class SubscriptionType(models.Model):
#     title = models.TextField(null=True, blank=False, verbose_name="Название")
#     duration = models.IntegerField(null=True, verbose_name="Длительность (дней)")
    
#     def __str__(self) -> str:
#         return self.title

#     class Meta:
#         verbose_name = "Вид подписки"
#         verbose_name_plural = "Виды подписки"

class Movie(models.Model):
    title = models.TextField(null=True, verbose_name="Название")
    duration = models.DurationField(null=True, verbose_name="Длительность")
    description = models.TextField(null=True, verbose_name="Описание")
    poster = models.ImageField(null=True, upload_to="movie-posters", verbose_name="Постер фильма")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class Category2Movie(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, null=True, verbose_name="Фильм")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, verbose_name="Категория подписки")

    def __str__(self) -> str:
        return self.movie.__str__() + ": " + self.category.__str__()

    class Meta:
        verbose_name = "Категория и фильм"
        verbose_name_plural = "Категории и фильмы"
    
class Category(models.Model):
    title = models.TextField(null=True, verbose_name="Название")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Категория подписки"
        verbose_name_plural = "Категории подписок"

class Subscription2Category(models.Model):
    subscription = models.ForeignKey("Subscription", on_delete=models.CASCADE, null=True, verbose_name="Подписка")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, verbose_name="Категория")

    def __str__(self) -> str:
        return self.subscription.__str__() + ": " + self.category.__str__()

    class Meta:
        verbose_name = "Категориа и подписка"
        verbose_name_plural = "Категории и подписки"

class Subscription(models.Model):
    title = models.TextField(null=True, verbose_name="Название")
    price = models.DecimalField(null=True, max_digits=7, decimal_places=2, verbose_name="Цена")
    duration = models.IntegerField(null=True, verbose_name="Длительность (дней)")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

class Subscription2User(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, verbose_name="Пользователь")
    subscription = models.ForeignKey("Subscription", on_delete=models.CASCADE, null=True, verbose_name="Подписка")
    date_subscription = models.DateField(default=timezone.now, verbose_name="Дата оформления подписки")
    # is_active = models.BooleanField(null=True, default=True, verbose_name="Статус подписки")

    class Meta:
        verbose_name = "Подписка пользователя"
        verbose_name_plural = "Подписки пользователей"

class UserProfile(models.Model):
    """Пользовательский профиль"""
    class Role(models.IntegerChoices):
        guest = 0
        admin = 1

        def __str__(self) -> str:
            return self.name()

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    role = models.IntegerField(choices=Role, verbose_name="Роль")
    account_money = models.DecimalField(null=True, max_digits=7, decimal_places=2, verbose_name="Деньги на счету")

    class Meta:
        verbose_name = "Пользовательский профиль"
        verbose_name_plural = "Пользовательские профили"