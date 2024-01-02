from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class Producer(models.Model):
    """ Модель производителя """

    title = models.CharField(max_length=250, verbose_name='Производитель', unique=True)
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=300, verbose_name='Страна')
    city = models.CharField(max_length=250, verbose_name='Город')
    street = models.CharField(max_length=300, verbose_name='Улица')
    house = models.CharField(max_length=250, verbose_name='Номер дома')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'


class Commodity(models.Model):
    """Модель товара"""
    title = models.CharField(max_length=250, verbose_name='Наименование'),
    version = models.CharField(max_length=300, verbose_name='Версия', **NULLABLE),
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания'),
    provider = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='Производитель')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Supplier(models.Model):
    """ Модель поставщика """
    DISTRIBUTOR = 'торговая сеть'
    IE = 'ИП'

    supplier_type = (
        (DISTRIBUTOR, 'торговая сеть'),
        (IE, 'ИП')
    )

    title = models.CharField(max_length=250, verbose_name='Производитель', unique=True)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    type = models.CharField(choices=supplier_type, verbose_name='Тип поставщика')
    country = models.CharField(max_length=300, verbose_name='Страна')
    city = models.CharField(max_length=250, verbose_name='Город')
    street = models.CharField(max_length=300, verbose_name='Улица')
    house = models.CharField(max_length=250, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'


class Supply(models.Model):
    """Модель поставки"""

    product = models.ForeignKey(Commodity, on_delete=models.CASCADE, verbose_name='Товар')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='Производитель')
    provider = models.ForeignKey(Supplier, related_name='related_supplier', on_delete=models.CASCADE,
                                 verbose_name='Поставщик', null=True, blank=True)
    recipient = models.ForeignKey(Supplier, related_name='related_recipient', on_delete=models.CASCADE,
                                  verbose_name='Получатель поставки', null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f'{self.product}, производитель {self.producer}, поставщик {self.provider}, '
                f'получатель {self.recipient}, дата {self.created_at}')

    class Meta:
        verbose_name = 'поставка'
        verbose_name_plural = 'поставки'
