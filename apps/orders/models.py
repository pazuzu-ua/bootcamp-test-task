from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    """Class that represents a Product."""

    class Meta:
        ordering = ('-created_at',)

    name = models.CharField(
        _('Product name'),
        max_length=35,
        db_index=True,
    )
    description = models.TextField(
        _('Product description'),
        max_length=400,
    )
    price = models.DecimalField(
        _('Product price'),
        max_digits=7,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
       _('Created at'), 
       auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'{self.name} ({self.id})'


class Order(models.Model):
    """Class that represents an Order."""

    class Meta:
        ordering = ('-created_at',)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField(
       _('Created at'), 
       auto_now=True,
    )

    def __str__(self) -> str:
        return f'Order No. {self.id}'
    
    def __repr__(self) -> str:
        return self.__str__
