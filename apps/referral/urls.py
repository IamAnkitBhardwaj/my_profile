from django.urls import path
from . import views

urlpatterns = [
    path('', views.referral, name='referral'),
    path('success/', views.referral_success, name='referral_success'),
]