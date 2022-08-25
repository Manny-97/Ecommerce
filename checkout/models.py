from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class DeliveryOptions(models.Model):
    DELIVERY_CHOICES = [("IS", "In Store"), ("HD", "Home Delivery"), ("DD", "Digital Delivery")]

    delivery_name = models.CharField(verbose_name=_("Delivery Name"), help_text=_("Required"), max_length=255)
    delivery_price = models.DecimalField(
        verbose_name=_("Delivery Price"),
        help_text=_("Maximum of 999.99"),
        error_messages={
            "name": {"max_length": _("The price must be between 0 and 999.99")},
        },
        max_digits=5,
        decimal_places=2,
    )
    delivery_methods = models.CharField(
        choices=DELIVERY_CHOICES, verbose_name=_("Delivery Method"), help_text=_("Required"), max_length=255
    )
    delivery_window = models.CharField(verbose_name=_("Delivery Window"), help_text=_("Required"), max_length=255)
    delivery_timeframe = models.CharField(verbose_name=_("Delivery Timeframe"), help_text=_("Required"), max_length=255)
    order = models.IntegerField(verbose_name=_("order list"), help_text=_("Required"))
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Delivery option")
        verbose_name_plural = _("Delivery options")

    def __str__(self) -> str:
        return self.delivery_name

class PaymentSelection(models.Model):
    name = models.CharField(verbose_name=_("name"), help_text=_("Required"), max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Payment selection")
        verbose_name_plural = _("Payment selections")

    def __str__(self) -> str:
        return self.name