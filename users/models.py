from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = PhoneNumberField(blank=True)
    city = models.CharField(max_length=35, blank=True, null=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Аватар')

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_data = models.DateTimeField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL,
                                    blank=True, null=True, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL,
                                    blank=True, null=True, verbose_name='оплаченный урок')
    payment_sum = models.IntegerField(default=0, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, choices=METHOD, verbose_name='способ оплаты', default='наличные')

    def __str__(self):
        return f'{self.user} - {self.paid_course if self.paid_course else self.paid_lesson} ({self.payment_sum})'

    class Meta:
        verbose_name = "платежи"
        verbose_name_plural = "платежи"

