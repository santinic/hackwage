from django.db import models


class Feedback(models.Model):
    sender_email = models.EmailField()
    message = models.CharField(max_length=10000)
    read = models.BooleanField(default=False)
