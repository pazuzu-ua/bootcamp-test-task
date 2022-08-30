from factory import Factory, Faker
from random import randint
from .models import Product


class ProductFactory(Factory):
    """This is a Product factory."""

    class Meta:
        model = Product
    
    name = Faker(
        'sentence', 
        nb_words=randint(1, 3), 
    )
    description = Faker(
        'paragraph', 
        nb_sentences=randint(1, 3),
    )
    price = Faker(
        'pyfloat', 
        left_digits=randint(1, 3),
        right_digits=0,
        positive=True,
    )
