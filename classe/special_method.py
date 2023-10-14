#  Copyright (c) 2022. Code by Dimitri AIGLE

class User():
    def __init__(self,email,name):
        self.name = name
        self.email = email

    def __str__(self):
        return f"User : { self.name}, {self.email}"

    def __eq__(self, other):
        return self.email == other.email

    def __call__(self, *args, **kwargs):
        print("bonjour !")

jean = User("jean@gmail.com","jean")
julie = User("julie@gmail.com","julie")

print(jean == julie)
print(julie.__str__())

jean()