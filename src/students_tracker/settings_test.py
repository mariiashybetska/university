import os

from students_tracker.settings import *

# CELERY_TASK_ALWAYS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'