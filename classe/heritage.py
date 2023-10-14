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
        print("User " +self.name+" init")

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

class Admin(User):

    # redefinition de la methode
    def __init__(self, prenom ,name ,age , email ,origin):
        self.origin = origin
        # User.__init__(self,prenom,name,age,email) ou
        super().__init__(prenom,name,age, email)


    def delete_user(self,user : User):
        print('delete user')

    #reference methode bonjour
    def bonjour(self):
        print("Bonjour je suis " +self.name.capitalize() +", admin de " + self.origin )

j = User("julie","burner",21,"julie@live.fr")
d = Admin("dimitri","aigle",22,"dimitriaigle@gmail.com","dyma")

# san redefinir de methode de la classe parente
d.delete_user(j)
d.bonjour()

# Verifier que un objet herite d'une classe
print(isinstance(d,object))
print(isinstance(d,Admin))
print(isinstance(d,User))

# Verifier un classe herite d'une autre classe
print(issubclass(Admin,User))
print(issubclass(User,Admin))
print(issubclass(int,object))
print(issubclass(User,object))