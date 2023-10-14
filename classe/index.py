#  Copyright (c) 2022. Code by Dimitri AIGLE



class User():
    def __init__(self, prenom: str, name : str, age : int, email : str):
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
        # print(self)

    def bonjour(self):
        print(f"Bonjour je suis {self.prenom}")

    # un "_" au debut d'une methode signifie attention cette methode est privé il ne faut pas la toucher
    def _say_hi(self):
        print("Bonjour Say hi")
    @classmethod
    def another_constructor(cls):
        return cls("No first name","No name",0,"No email")
    @staticmethod
    def add_ages(a: int,b: int):
        return a.age + b.age

d = User("dimitri","aigle",22,"dimitriaigle@gmail.com")
j = User("julie","burner",21,"julie@live.fr")
c = User.another_constructor()


d.bonjour()
print(d.name,d.prenom,d.age,d.email)
print(j.name,j.prenom,j.age,j.email)

print(c.name,c.prenom,c.age,c.email)

print(User.add_ages(d,j))

#afficher tous les attribut d'un objet "dir()"
print(dir(User))
