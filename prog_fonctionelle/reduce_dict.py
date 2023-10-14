#  Copyright (c) 2022. Code by Dimitri AIGLE
from functools import reduce

panier = [
    {
        "name": "chaussures",
        "price": 55,
        "quantity": 1
    }, {
        "name": "livre",
        "price": 10,
        "quantity": 2
    }, {
        "name": "cookie",
        "price": 5,
        "quantity": 3
    }
]


def fn(acc, item):
    acc['total_price'] += item['price'] * item['quantity']
    acc['total_quantity'] += item['quantity']
    return acc


total = reduce(fn, panier, {'total_price': 0, 'total_quantity': 0})
print(total)  #  {'total_price': 90, 'total_quantity': 6}