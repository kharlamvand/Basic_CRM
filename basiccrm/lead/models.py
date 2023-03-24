from django.contrib.auth.models import User
from django.db import models

from team.models import Team


class Lead(models.Model):
    LOW = 'Низкий'
    MEDIUM = 'Средний'
    HIGH = 'Высокий'

    CHOICES_PRIORITY = (
        (LOW, 'Низкий'),
        (MEDIUM, 'Средний'),
        (HIGH, 'Высокий')
    )

    NEW = 'Открыта'
    CONTACTED = 'В работе'
    WON = 'Выполнена'
    LOST = 'Отклонена'

    CHOICES_STATUS = (
        (NEW, 'Открыта'),
        (CONTACTED, 'В работе'),
        (WON, 'Выполнена'),
        (LOST, 'Отклонена'),
    )

    team = models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE, verbose_name='Команда')
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField()
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM, verbose_name='Приоритет')
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW, verbose_name='Статус')
    converted_to_client = models.BooleanField(default=False, verbose_name='Конвертировать в клиента')
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE, verbose_name='Создана')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана в')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Изменена в')

    class Meta:
        ordering = ('name',)
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.name


class LeadFile(models.Model):
    team = models.ForeignKey(Team, related_name='lead_files', on_delete=models.CASCADE, verbose_name='Команда')
    lead = models.ForeignKey(Lead, related_name='files', on_delete=models.CASCADE, verbose_name='Заявка')
    file = models.FileField(upload_to='leadfiles', verbose_name='Файл')
    created_by = models.ForeignKey(User, related_name='lead_files', on_delete=models.CASCADE, verbose_name='Создан')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан в')

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.created_by.username


class Comment(models.Model):
    team = models.ForeignKey(Team, related_name='lead_comments', on_delete=models.CASCADE, verbose_name='Команда')
    lead = models.ForeignKey(Lead, related_name='comments', on_delete=models.CASCADE, verbose_name='Заявка')
    content = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_by = models.ForeignKey(User, related_name='lead_comments', on_delete=models.CASCADE, verbose_name='Создана')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана в')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.created_by.username
