from django.urls import path

from . import views

urlpatterns = [
    path('', views.BasketView, name='basket'),
    path('orderolaced/', views.order_placed, name='order_placed'),
    path('error/', views.Error.as_view(), name='error'),
    path('webhook/', views.stripe_webhook),
]
