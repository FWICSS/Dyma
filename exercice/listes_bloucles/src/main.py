def fonction_test(note):
    nombres = note
    nombres_pairs = []

    for i in range(0, len(note)):
        if(nombres[i] % 2 == 0):
            nombres_pairs.append(nombres[i])

    return nombres_pairs