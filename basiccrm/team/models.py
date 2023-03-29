from django.contrib.auth.models import User
from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=50)  # , verbose_name='Название'
    price = models.IntegerField()  # verbose_name='Стоимость'
    description = models.TextField(blank=True, null=True)  # , verbose_name='Описание'
    max_leads = models.IntegerField()  # verbose_name='Максимальное количество заявок'
    max_clients = models.IntegerField()  #verbose_name='Максимальное количество клиентов'

    # class Meta:
    #     verbose_name = "Тарифный план"
    #     verbose_name_plural = "Тарифные планы"

    def __str__(self):
        return self.name


class Team(models.Model):
    plan = models.ForeignKey(Plan, related_name='teams', blank=True, null=True, on_delete=models.CASCADE)  #  , verbose_name='Тарифный план'
    name = models.CharField(max_length=100)  # , verbose_name='Название'
    members = models.ManyToManyField(User, related_name='teams')  # , verbose_name='Участники'
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)  #  , verbose_name='Создан'
    created_at = models.DateTimeField(auto_now_add=True)  # , verbose_name='Создан в '

    # class Meta:
    #     verbose_name = "Команда"
    #     verbose_name_plural = "Команды"

    def __str__(self):
        return self.name
