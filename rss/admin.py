from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('sender_email', 'read')


admin.site.register(Feedback, FeedbackAdmin)
