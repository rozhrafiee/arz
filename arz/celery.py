import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arz.settings')

app = Celery('arz')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()