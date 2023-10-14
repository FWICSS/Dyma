#  Copyright (c) 2022. Code by Dimitri AIGLE
li = [1, 2, 3, 4, 55, 23, 11, 10, 18]


def pair(item):
    return item % 2 == 0


iterateur = filter(pair, li, )

print(list(iterateur))  # [2, 4, 10, 18]

li = [1, 'a', '', [], {}, 0, False, True, '0']


iterateur = filter(None, li)

print(list(iterateur))  # [1, 'a', True, '0']