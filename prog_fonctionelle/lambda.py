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

a = [1, 2, 3]

b = list(map(lambda item : item *2, a))

print(b)

total = reduce(lambda acc, item: acc +
                item['price'] * item['quantity'], panier, 0)
print(total)  #  90

li = [1, 2, 3, 4, 55, 23, 11, 10, 18]


iterateur = filter(lambda x: x % 2 == 0, li)

print(list(iterateur))  # [2, 4, 10, 18]

def multiply_by(factor):
    return lambda item: factor * item


double = multiply_by(2)
print(double(5))  # 10