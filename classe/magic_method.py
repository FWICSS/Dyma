#  Copyright (c) 2022. Code by Dimitri AIGLE

class User():
    '''Une classe super utile'''
    def __init__(self,name,email):
        self.name = name
        self.email = email

jean = User('jean','jean@gmail.com',)
julie = User('jean','julie@gmail.com')
print("1. ",end="")
print(jean.__dir__())
print("2. " + User.__doc__)
