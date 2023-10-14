#  Copyright (c) 2022. Code by Dimitri AIGLE
import re

match = re.search(r'(^\w+)\.([a-z]{3}$)',
                  'mon_super_fichier.pdf')
print(match.group(0))  # mon_super_fichier.pdf

print(match.group(1))  # mon_super_fichier

print(match.group(2))  # pdf
print(match.groups())  # ('mon_super_fichier', 'pdf')


#nommé les groupes
match = re.search(r'(?P<nom>^\w+)\.(?P<extension>[a-z]{3}$)',
                  'mon_super_fichier.pdf')

print(match.group('nom'))  # mon_super_fichier.pdf
print(match.group('extension'))  # pdf

# sous groupe
import re

match = re.search(r'(?P<date>(?P<jour>\d{2})\/\d{2}\/(?P<annee>\d{4})) à (?P<heure>\d{2}:\d{2}:\d{2})',
                  '29/10/2022 à 10:16:30')

print(match.group('date'))  # 29/10/2022
print(match.group('jour'))  # 29
print(match.group('annee'))  # 2022
print(match.group('heure'))  # 10:15:30

import re

regex = re.compile(
    r'(?=.*[a-z]+.*)(?=.*[A-Z]+.*)(?=.*[0-9]+.*)(?=.*[\W_]+.*)(?!.*\s).{10,}')

print(regex.match('hello'))  # None
print(regex.match('hello123'))  # None
print(regex.match('hello123!'))  # None
print(regex.match('he123!A'))  # None
print(regex.match('Ahello@123!'))  # None
print(regex.match('Ahello123!'))
# <re.Match object; span=(0, 14), match='hello123!Aezfz'>