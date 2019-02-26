from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('job/', views.job),
    path('job/<title>/', views.job),
    path('search/', views.search),
    path('popular/<name>/', views.popular),
    path('feedback/', views.feedback_create),
    path('feedback/thanks', views.feedback_thanks)
]