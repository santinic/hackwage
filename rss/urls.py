from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('item/', views.item),
    path('search/', views.search),
    path('feedback/', views.feedback_create, name='feedback_create'),
    path('feedback/thanks', views.feedback_thanks),
]