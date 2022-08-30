import logging
from celery import Celery
from django.shortcuts import get_object_or_404
from django.http import Http404
from .factories import ProductFactory
from .models import Product


logger = logging.getLogger(__name__)
app = Celery()


@app.task
def random_product():
    """Create a random Product."""
    product = ProductFactory.build()
    logger.info(f'{product} was created.')
    product.save()

@app.task
def big_brother(key: str):
    """Spooky function that stalks Customers."""
    try:
        product = get_object_or_404(Product, pk=key)
        print(f'Big bother is watching... You have just looked at "{product.name}"')
    except Http404:
        print('Big Brother failed this time, but he is still watching...')
