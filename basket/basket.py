class Basket():
    """A base Basket class, providing some behavior that can be inherited or overriden, as necessary"""

    def __init__(self, request):

        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {'price':str(product.price), 'qty': int(qty)}

        self.session.modified = True

    def __len__(self):
        """Get basket and count quantity of items"""
        return sum(item['qty'] for item in self.basket.values())