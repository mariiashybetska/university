from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import Student

import string


@receiver(pre_save, sender=Student)
def pre_save_student(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    instance.first_name = string.capwords(instance.first_name)
    instance.last_name = string.capwords(instance.last_name)
    instance.telephone = ''.join(x for x in instance.telephone if x.isdigit())

    if instance.id is None:
        print('Object is created!')
