#  Copyright (c) 2022. Code by Dimitri AIGLE
a = [1, 2, 3]

# b = [c for c in a]
#
# d = (c for c in a)
#
# print(b)
# print(list(d))

#b = list(map(lambda x: x**2, a))

# b = [val**2  for val in a]
# c = [num for num in range(100)]
# d = [num for num in range(100) if num % 2 != 0]
#
#
#
# print(b)
# print(c)
# print(d)

# [
#     [' . ',' . ',' . '],
#     [' . ',' . ',' . '],
#     [' . ',' . ',' . '],
# ]
e = [' . ' for i in range(3)]
print(e)

f = [[j + i * 3 for j in range(3)] for i in range(3)]

print(f)