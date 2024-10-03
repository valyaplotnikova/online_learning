from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from materials.models import Course, Lesson


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = PhoneNumberField(**NULLABLE)
    city = models.CharField(max_length=35, **NULLABLE, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatars/', **NULLABLE, verbose_name='Аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Payments(models.Model):
    METHOD = [
        ('наличные', 'наличные'),
        ('перевод на счет', 'перевод на счет')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    payment_data = models.DateTimeField(**NULLABLE, verbose_name='дата оплаты')
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL,
                                    **NULLABLE, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL,
                                    **NULLABLE, verbose_name='оплаченный урок')
    payment_method = models.CharField(max_length=50, choices=METHOD, verbose_name='способ оплаты', default='наличные')
    session_id = models.CharField(max_length=255, verbose_name='ID сессии', **NULLABLE)
    link_to_payment = models.URLField(max_length=400, verbose_name='ссылка на оплату', **NULLABLE)
    payment_status = models.CharField(max_length=400, verbose_name='ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.paid_course if self.paid_course else self.paid_lesson} ({self.payment_sum})'

    class Meta:
        verbose_name = "платежи"
        verbose_name_plural = "платежи"

