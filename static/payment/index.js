var stripe = Stripe('publishable_api_key');

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

var elements = stripe.elements();
var style = {
    base: {
        color: "#000",
        lineHeight: '2.4',
        fontSize: '16px'
    }
};
var card = elements.create('card', { style: style });
card.mount('#card-element');

card.on('change', function(event) {
    var displayError = document.getElementById('card-erros')
    if (event.error) {
        displayError.textContent = event.error.message;
        $('#card-errors').addClass('alert alert-info');
    } else {
        displayError.textContent = '';
        $('#card-erros').removeClass('alert alert-info');
    }
})