#  Copyright (c) 2022. Code by Dimitri AIGLE
from io import UnsupportedOperation

with open("fichier.txt","w") as fichier:
    try:
        fichier.write("Bonjour !\n")
    except UnsupportedOperation:
        print("Manque de permission")

saisons = ["été", "hivers", "automne", "printemps"]
with open("test.txt", "w") as fichier:
  for saison in saisons:
      fichier.write(f"{saison}")