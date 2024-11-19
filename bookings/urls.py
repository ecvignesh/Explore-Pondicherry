from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='booking_list'),
    path('payment-success/', views.payment_success, name='payment_success'),
]
