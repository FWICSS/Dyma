def trier_cles(dictionnaire):
    cles_numeriques = []
    cles_chaines = []

    for key in dictionnaire:
        if isinstance(dictionnaire[key], (int, float)):
            cles_numeriques.append(key)
        elif isinstance(dictionnaire[key], str):
            cles_chaines.append(key)

    return cles_numeriques, cles_chaines

