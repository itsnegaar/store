from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

broker_url = 'amqp://guest:guest@localhost:5672//'

app = Celery('store')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.autodiscover_tasks()
app.conf.beat_schedule = {
    'update-product-counts': {
        'task': 'shopino.tasks.update_product_counts',
        'schedule': crontab(minute='*/1'),  # Every 1 minute
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
