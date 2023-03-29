import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'news-parser': {
        'task': 'blog.tasks.quotes_parser',
        'schedule': crontab()
        # 'schedule': crontab(hour='*/6')
    },
}
