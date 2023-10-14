def trier_liste(melange):
    # Listes vides pour stocker les nombres et les chaînes
    nombres = []
    chaines = []

    for element in melange:

        if type(element) == str:
            chaines.append(element)
        else:
            nombres.append(element)

        chaines.sort()
        nombres.sort()

    return chaines, nombres


