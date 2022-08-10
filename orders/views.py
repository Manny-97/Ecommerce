from django.shortcuts import render
from basket.basket import Basket
from django.http.response import JsonResponse
from .models import Orders
# Create your views here.

def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        order_key = request.POST.get('order_key')
        user_id = request.user.id
    response = JsonResponse({})
    return response

def payment_confirmation(data):
    Orders.objects.filter(order_key=data).update(billing_status=True)

def user_orders(request):
    user_id = request.user.id
    orders = Orders.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders