#  Copyright (c) 2022. Code by Dimitri AIGLE
li = [1, 2, 3]
li2 = [4, 5, 6, 7]


def multiply_by_2(item1, item2):
    return item1 * item2


iterateur = map(multiply_by_2, li, li2)

print(list(iterateur)) # [4, 10, 18]