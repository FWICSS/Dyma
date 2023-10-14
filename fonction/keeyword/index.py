#  Copyright (c) 2022. Code by Dimitri AIGLE
def foo_out():
    total =0

    def foo():
        nonlocal total
        print(total)
        total+=1
    return foo


a = foo_out()
a()
a()
a()