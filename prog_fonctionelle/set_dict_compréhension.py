#  Copyright (c) 2022. Code by Dimitri AIGLE
a = [1, 2, 3]

c = {c for c in a}

d = {num for num in range(100)}

# Pas de set dans un set

print(c)
print(d)

#b = { item: index + 1 for index,item in enumerate('abc')}
b = { i: i**i for i in range(10)}

print(b)