from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Subscription


@shared_task
def send_email_about_update(course_id):
    """
        Отправляем сообщение об обновлении курса
        :param course_id: идентификатор курса
        """
    subs = Subscription.objects.filter(course=course_id)
    for sub in subs:
        course = sub.course
        user = sub.owner
        send_mail(
            subject=f'{course} обновился',
            message=f'{course} был обновлен. Посмотреть подробности можно на сайте',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )

