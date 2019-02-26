from django.contrib.flatpages import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('job/', views.job),
    path('job/<title>/', views.job),
    path('search/', views.search),
    path('popular/<name>/', views.popular),
    path('feedback/', views.feedback_create),
    path('feedback/thanks', views.feedback_thanks),
    path('data-sources/', views.data_sources)
]