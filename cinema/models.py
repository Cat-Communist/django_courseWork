from django.db import models

# Create your models here.
class SubscriptionType(models.Model):
    title = models.TextField(blank=True, verbose_name="Название")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Вид подписки"
        verbose_name_plural = "Виды подписки"

class Subscription(models.Model):
    type = models.ForeignKey("SubscriptionType", on_delete=models.CASCADE, null=True, verbose_name="Вид подписки")
    # Как хранить время подписки
    duration = models.DurationField(null=True, verbose_name="Длительность")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

class Movie(models.Model):
    title = models.TextField(blank=True, verbose_name="Название")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, verbose_name="Жанр фильма")
    duration = models.DurationField(null=True, verbose_name="Длительность")
    rating = models.FloatField(null=True, verbose_name="Оценка")

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class Category(models.Model):
    title = models.TextField(blank=True, verbose_name="Название")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

# TODO: таблица-связь подписки и пользователя (в схеме "Сам факт")