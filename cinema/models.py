from datetime import timezone

from django.db import models

# Create your models here.
class SubscriptionType(models.Model):
    title = models.TextField(null=True, blank=False, verbose_name="Название")
    duration = models.IntegerField(null=True, verbose_name="Длительность (дней)")
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Вид подписки"
        verbose_name_plural = "Виды подписки"

class Subscription(models.Model):
    type = models.ForeignKey("SubscriptionType", on_delete=models.CASCADE, null=True, verbose_name="Вид подписки")
    category = models.ForeignKey("Category", null=True, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(null=True, max_digits=7, decimal_places=2, verbose_name="Цена")

    def __str__(self) -> str:
        return self.type.__str__() + ": " + self.category.__str__()
    
    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

class Movie(models.Model):
    title = models.TextField(null=True, blank=False, verbose_name="Название")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, verbose_name="Категория подписки")
    duration = models.DurationField(null=True, verbose_name="Длительность")
    description = models.TextField(null=True, verbose_name="Описание")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class Category(models.Model):
    title = models.TextField(null=True, blank=False, verbose_name="Название")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Категория подписки"
        verbose_name_plural = "Категории подписок"

class UserSubscription(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, verbose_name="Пользователь")
    subscription = models.ForeignKey("Subscription", on_delete=models.CASCADE, null=True, verbose_name="Подписка")
    last_payment = models.DateField(auto_now=True, verbose_name="Дата последнего списания")
    # next_payment = models.DateField(default=last_payment+subscription) # TODO: то ж как и на last_payment + как обращаться к полям других таблиц (для рассчёта следующей оплаты)
    is_active = models.BooleanField(null=True, default=True, verbose_name="Статус подписки")

    class Meta:
        verbose_name = "Подписка пользователя"
        verbose_name_plural = "Подписки пользователей"