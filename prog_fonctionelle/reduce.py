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
    return acc + item['price'] * item['quantity']


total = reduce(fn, panier, 0)
print(total)  #  90