from django.conf import settings

import django
from distutils.version import LooseVersion, StrictVersion

if StrictVersion(django.get_version()) >= StrictVersion("1.7"):
    from django.utils.module_loading import import_string
else:
    from django.utils.module_loading import import_by_path as import_string

BACKEND = getattr(settings, 'CELERY_PROGRESS_BACKEND',
                  'celery_progress.backends.CeleryBackend')


def get_backend():
    return import_string(BACKEND)


backend = get_backend()()
