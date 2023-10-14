#  Copyright (c) 2022. Code by Dimitri AIGLE
from translate import Translator
translator= Translator(to_lang="en",from_lang="fr")

with open("project.txt", 'a', encoding="utf-8") as file:
    while True:
        text = input(">")
        if text == "quit":
            break
        file.write(translator.translate(text) + "\n")
        file.flush()
print("Bye")