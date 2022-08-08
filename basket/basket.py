


class Basket():
    """A base Basket class, providing some behavior that can be inherited or overriden, as necessary"""

    def __init__(self, request):

        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket