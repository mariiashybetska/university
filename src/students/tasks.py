from celery import shared_task
from time import sleep
from datetime import timedelta, datetime

from django.core.mail import send_mail
from django.conf import settings

from students.models import Logger



@shared_task
def add(a, b):
    print('ADD WORKS!')
    sleep(10)
    print(a + b)
    return a + b


@shared_task
def send_email_async(subject, message,
                     email_from):

    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message,
              email_from, recipient_list,
              fail_silently=False)


# @shared_task
# def delete_logs_test():
#     Logger.objects.all().delete()


@shared_task
def delete_logs():
    td = timedelta(days=-7)
    Logger.objects.filter(created__lte=datetime.now() + td).delete()


