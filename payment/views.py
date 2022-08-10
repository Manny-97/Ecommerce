import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import os
from orders.views import payment_confirmation
from django.http.response import HttpResponse
import json
from basket.basket import Basket
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    print(total)
    # Stripe doesnt accept decimal, hence the need to convert to integer
    total = int(total.replace('.', ''))
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    intent = stripe.PaymentIntent.create(amount=total, currency='gbp', metadata={'userid': request.user.id})
    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})


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