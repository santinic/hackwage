# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings
#
#
# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj.shared_settings')
#
# app = Celery('dj')
#
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
#
#
# # @app.task(bind=True)
# # def debug_task(self):
# #     print('Request: {0!r}'.format(self.request))
