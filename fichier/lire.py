#  Copyright (c) 2022. Code by Dimitri AIGLE
# file_object = open("fichier.txt","r")
#
# print(file_object)
#
# file_object.close()
with open("fichier.txt", "r") as fichier:
    text = fichier.readlines()
    texte = "".join(text)
    print(texte)
    # for line in fichier:
    #     print(line, end="")