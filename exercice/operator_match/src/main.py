def fonction_test(note):
    # déclarez en dessous :
    if(int(note) == 5): return "Excellent"
    if(int(note) == 4) : return"Très bien"
    if(int(note) == 3) : return "Bien"
    if(int(note) == 2) : return "Moyen"
    if(int(note) == 0 or int(note) == 1) : return "Médiocre"


    # ne touchez pas au return.
    return "La note doit être un nombre compris entre 0 et 5"