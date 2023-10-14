#  Copyright (c) 2022. Code by Dimitri AIGLE
# li1 = ['id', 'name', 'email']
# li2 = [1, 'jean', 'jean@gmail.com']
#
# print(dict(zip(li1, li2)))
# {'id': 1, 'name': 'jean', 'email': 'jean@gmail.com'}

li1 = [1, 2, 3]
li2 = [4, 5, 6, 7]
li3 = [7, 8, 9, 10]

print(list(zip(li1, li2, li3)))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)

# Vous pouvez également passer l'option strict=True si vous souhaitez que Python renvoie une erreur si les listes n'ont pas le même nombre d'éléments 
# li1 = [1, 2, 3]
# li2 = [4, 5, 6, 7]
# li3 = [7, 8, 9, 10]
#
# print(list(zip(li1, li2, li3, strict=True)))
# # ValueError: zip() argument 2 is longer than argument 1