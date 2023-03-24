from django.contrib.auth.models import User
from django.db import models

from team.models import Team


class Client(models.Model):
    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE, verbose_name='Команда')
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField()
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE, verbose_name='Создан')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан в')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Изменен в')

    class Meta:
        ordering = ('name',)
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.name


class Comment(models.Model):
    team = models.ForeignKey(Team, related_name='client_comments', on_delete=models.CASCADE, verbose_name='Команда')
    client = models.ForeignKey(Client, related_name='comments', on_delete=models.CASCADE, verbose_name='Клиент')
    content = models.TextField(blank=True, null=True, verbose_name='Добавить комментарий')
    created_by = models.ForeignKey(User, related_name='client_comments', on_delete=models.CASCADE, verbose_name='Создано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано в')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.created_by.username


class ClientFile(models.Model):
    team = models.ForeignKey(Team, related_name='client_files', on_delete=models.CASCADE, verbose_name='Команда')
    client = models.ForeignKey(Client, related_name='files', on_delete=models.CASCADE, verbose_name='Клиент')
    file = models.FileField(upload_to='clientfiles', verbose_name='Файл')
    created_by = models.ForeignKey(User, related_name='client_files', on_delete=models.CASCADE, verbose_name='Создан')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан в')

    def __str__(self):
        return self.created_by.username