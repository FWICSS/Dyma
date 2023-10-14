

def ajouter_contact(repertoire: dict, nom: str, numero: str):
    repertoire[nom] = numero
    return repertoire

def supprimer_contact(repertoire: dict, nom: str):
    if nom in repertoire:
        del repertoire[nom]
    return repertoire

def rechercher_contact(repertoire: dict, nom: str):
    return repertoire.get(nom, "Contact non trouvé")
