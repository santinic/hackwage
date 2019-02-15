from django.db import models
from django.forms import ModelForm


# class Item(models.Model):
#     title = models.TextField()
#     body = models.TextField()
#     body_html = models.TextField()


class Feedback(models.Model):
    sender_email = models.EmailField()
    # data_source_url = models.URLField()
    message = models.CharField(max_length=10000)
    read = models.BooleanField(default=False)


# class FeedbackForm(ModelForm):
#     your_name = forms.CharField(label='Your name', max_length=100)
#     sender = forms.EmailField()
#     data_source_url = forms.URLField(label="Data Source URL")
#     message = forms.CharField(label="Feedback Message", widget=forms.Textarea)
#
#     class Meta:
#         model = Feedback
