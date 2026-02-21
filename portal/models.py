from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        validators=[RegexValidator(r'^[А-Яа-яЁё\s-]+$', 'Допустимы только кириллица, пробелы и дефис.')],
    )
    phone = models.CharField(
        max_length=16,
        unique=True,
        verbose_name='Телефон',
        validators=[RegexValidator(r'^8\(\d{3}\)\d{3}-\d{2}-\d{2}$', 'Формат: 8(XXX)XXX-XX-XX')],
    )
    email = models.EmailField(unique=True, verbose_name='E-mail')

    REQUIRED_FIELDS = ['email', 'full_name', 'phone']

    def __str__(self):
        return self.username


class Application(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        REVIEW = 'review', 'На рассмотрении'
        APPROVED = 'approved', 'Одобрена'
        REJECTED = 'rejected', 'Отклонена'

    class ParticipationFormat(models.TextChoices):
        OFFLINE = 'offline', 'Офлайн'
        ONLINE = 'online', 'Онлайн'
        HYBRID = 'hybrid', 'Гибрид'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    title = models.CharField(max_length=255, verbose_name='Проект/мероприятие')
    event_date = models.DateField(verbose_name='Желаемая дата')
    genre = models.CharField(max_length=120, verbose_name='Жанр музыки')
    participation_format = models.CharField(
        max_length=20,
        choices=ParticipationFormat.choices,
        default=ParticipationFormat.OFFLINE,
        verbose_name='Формат участия',
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.title} ({self.get_status_display()})'
