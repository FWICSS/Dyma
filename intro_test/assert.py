#  Copyright (c) 2022. Code by Dimitri AIGLE
def add(a, b):
    assert isinstance(a, int) and isinstance(b, int), "A et/ou b ne sont pas des entier"
    return a + b


print(add(2, "3"))
