import json
import os

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from basket.basket import Basket
from orders.views import payment_confirmation

# Create your views here.


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    print(total)
    # Stripe doesnt accept decimal, hence the need to convert to integer
    total = int(total.replace('.', ''))
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(amount=total, currency='gbp', metadata={'userid': request.user.id})
    return render(request, 'payment/payment_form.html', {'client_secret': intent.client_secret, 
                                                        'STRIPE_PUBLISHABLE_KEY': os.environ.get('STRIPE_PUBLISHABLE_KEY')})


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None
    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)
    if event.type == 'payment_intent.succeed':
        payment_confirmation(event.data.object.client_secret)

    else:
        print("Unhandled event type {}".format(event.type))
    return HttpResponse(status=200)