#  Copyright (c) 2022. Code by Dimitri AIGLE

# power = 2
#
# def power_factor(power):
#         return number ** power
#     return power_by
#
# power_by_2 = power_factor(2)
#
# print(power_by_2(2))
# print(power_by_2(3))


def foo():
    arr = []
    for item in range(3):
        def display():
            print(item)
        arr.append(display)
    return arr

a = foo()

a[0]()
a[1]()
a[2]()