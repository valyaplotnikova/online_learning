from django.conf import settings
from django.db import models


class Course(models.Model):
    """Модель курса."""
    course_name = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course/image', blank=True, null=True, verbose_name='Картинка для курса')
    description = models.TextField(blank=True, null=True, verbose_name='Описание курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='Владелец курса')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Время создания курса')
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Время обновления курса')

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ("course_name",)


class Lesson(models.Model):
    """Модель урока."""
    lesson_name = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(blank=True, null=True, verbose_name='Описание урока')
    preview = models.ImageField(upload_to='lesson/image', blank=True, null=True, verbose_name='Картинка для урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Название курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='Владелец урока')
    url_video = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ссылка на видео урока')

    def __str__(self):
        return self.lesson_name

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ("lesson_name",)


class Subscription(models.Model):
    """Модель подписки."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Название курса')

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"

    def __str__(self):
        return f"{self.user} - {self.course}"
