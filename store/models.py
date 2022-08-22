from enum import Flag
from itertools import product
from tabnanny import verbose
from unicodedata import category

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

# Category table
class Category(MPTTModel):
    """Category Table implemented with MPTT"""

    name = models.CharField(
        verbose_name=_("Category Name"), max_length=255, unique=True, help_text=_("Required and Unique")
    )
    slug = models.SlugField(verbose_name=_("Category safe url"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class MPTTMETA:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self) -> str:
        return self.name


class ProductType(models.Model):
    """A table with the different list of products available for sale"""

    name = models.CharField(verbose_name=_("Product Name"), max_length=255, help_text=_("Required"), unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self) -> str:
        return self.name


class ProductSpecification(models.Model):
    """ """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """The Product table containing all product items"""

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(verbose_name=_("title"), help_text=_("required"), max_length=255)
    description = models.CharField(verbose_name=_("Description"), help_text=_("Not Required"), blank=True, max_length=300)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular Price"),
        help_text=_("Maximum of 999.99"),
        max_digits=5,
        decimal_places=2,
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99"),
            },
        },
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount Price"),
        help_text=_("Maximum of 999.99"),
        max_digits=5,
        decimal_places=2,
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99"),
            },
        },
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"), help_text=_("Change product visibility"), default=True
    )
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self) -> str:
        return self.title


class ProductSpecificationValue(models.Model):
    """ """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(verbose_name=_("value"), max_length=255)

    class Meta:
        verbose_name = _("Product specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self) -> str:
        return self.value


class ProductImage(models.Model):
    """ """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(verbose_name=_("Image"), help_text=_("Upload a product image"), upload_to="images/", default="images/default.png")
    alt_text = models.CharField(verbose_name=_("Alternative text"), help_text=_("Please add alternative text"), max_length=255, null=True, blank=True)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")