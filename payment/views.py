import stripe
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket
# Create your views here.

@login_required
def Basketview(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    # Stripe doesnt accept decimal, hence the need to convert to integer
    total = int(total.replace('.', ''))
    stripe.api_key = 'secret_key'
    intent = stripe.PaymentIntent.create(
        amount = total,
        currency = 'gbp',
        metadata = {'userid': request.user.id}
    )
    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})