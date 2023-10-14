#  Copyright (c) 2022. Code by Dimitri AIGLE
from typing import Any


def addtion_plus_one(a: int, b: int) -> int:
    '''
    info: fonction addition de deux nombres plus 1
    :param a: entier
    :param b:
    :return: nombre additioner plus 1
    '''
    def addition():
        return a + b +1
    return addition

a = addtion_plus_one(1,2)

print(addtion_plus_one.__doc__)