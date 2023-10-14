a = 1


def foo():
    def bar():
        print(a)
    bar()
    #print(sum([1,2]))


foo()