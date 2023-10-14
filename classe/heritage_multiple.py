#  Copyright (c) 2022. Code by Dimitri AIGLE

class User():
    def __init__(self, prenom: str, name: str, age: int, email: str):
        """
        methode constructeur de user
        :param prenom: prenom de utilisateur
        :param name: nom de l'utilisateur
        :param age: age de l'utilisateur
        :param email: email de l'utilisateur
        """
        self.name = name
        self.prenom = prenom
        self.email = email
        self.age = age
        print("User " + self.name + " init")

    def bonjour(self):
        print(f"Bonjour je suis {self.prenom}")

    # un "_" au debut d'une methode signifie attention cette methode est privé il ne faut pas la toucher
    def _say_hi(self):
        print("Bonjour Say hi")

    @classmethod
    def another_constructor(cls):
        return cls("No first name", "No name", 0, "No email")

    @staticmethod
    def add_ages(a: int, b: int):
        return a.age + b.age


class Hacker():
    def ddos(self, ip: str):
        print(f"ddos launch on {ip}")


class Admin(User,Hacker):

    # redefinition de la methode
    def __init__(self, prenom: str, name: str, age: int, email: str, origin: str):
        self.origin = origin
        # User.__init__(self,prenom,name,age,email) ou
        super().__init__(prenom, name, age, email)

    def delete_user(self, user: User):
        print('delete user')

    # reference methode bonjour
    def bonjour(self):
        print("Bonjour je suis " + self.name.capitalize() + ", admin de " + self.origin)


j = User("julie", "burner", 21, "julie@live.fr")
d = Admin("dimitri", "aigle", 22, "dimitriaigle@gmail.com", "dyma")

d.ddos("192.1.128.1.1")