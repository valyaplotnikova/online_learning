from django.conf import settings
from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course/image', blank=True, null=True, verbose_name='Картинка для курса')
    description = models.TextField(blank=True, null=True, verbose_name='Описание курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='Владелец курса')

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ("course_name",)


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(blank=True, null=True, verbose_name='Описание урока')
    preview = models.ImageField(upload_to='lesson/image', blank=True, null=True, verbose_name='Картинка для урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Название курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='Владелец урока')

    def __str__(self):
        return self.lesson_name

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ("lesson_name",)
