import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basket.basket import Basket

# Create your views here.


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    print(total)
    # Stripe doesnt accept decimal, hence the need to convert to integer
    total = int(total.replace('.', ''))
    stripe.api_key = ""
    intent = stripe.PaymentIntent.create(amount=total, currency='gbp', metadata={'userid': request.user.id})
    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')
