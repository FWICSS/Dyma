def calculer_statistiques(liste_eleves):
    # votre implémentation

    if(not liste_eleves):
        return "La liste est vide"

    notes = [note for _, note in liste_eleves]
    if not notes:
        return "La liste ne contient pas de notes"

    note_min = min(notes)
    note_max = max(notes)
    note_moyenne = round(sum(notes) / len(notes), 1)

    return (note_min, note_max, note_moyenne)

