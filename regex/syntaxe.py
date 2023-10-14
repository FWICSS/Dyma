import re

regex = re.compile('motif')

chaine = 'Je suis une chaîne de caractères contenant motif'

match = regex.search(chaine)

print(match)# <re.Match object; span=(43, 48), match='motif'>

# Utilisation sur une expression régulière compilée :
match = regex.search(chaine)

# Utilisation depuis le module regex
match2 = re.search('motif', chaine)

print(match)
print(match2)
# <re.Match object; span=(43, 48), match='motif'>

print(match.start())  #  43
print(match.end())  # 48
print(match.span())  #  (43, 48)

#findall() toutes les occurences
matches = regex.findall(chaine)

print(matches)  # ['motif', 'motif']

# finditer() renvoie un itérateur contenant des objets de correspondance
matches = regex.finditer(chaine)

for match in matches:
    print(match)

chaine = 'Je suis une chaîne de caractères contenant un motif plusieurs fois et motif.'
chaine2 = 'motif, je suis une chaîne de caractères'

match = regex.match(chaine)
print(match)  #  None

match2 = regex.match(chaine2)
print(match2)  #  <re.Match object; span=(0, 5), match='motif'>