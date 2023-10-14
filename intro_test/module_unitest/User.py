#  Copyright (c) 2022. Code by Dimitri AIGLE
class User:
    def __init__(self,adresse,name):
        self.adresse = adresse
        self.name = name

    def greeting(self):
        return f"Bonjour {self.name}"

    def get_adresse(self):
        return f"{self.adresse.country} : {self.adresse.city}"