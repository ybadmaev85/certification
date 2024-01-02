from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):

    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_active = models.BooleanField(default=False, verbose_name='Активен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'