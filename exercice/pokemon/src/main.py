def creer_equipe(*pokemon: str):
    pokemons = []
    for p in pokemon:
        pokemons.append(p)
    return pokemons

def afficher_equipe(equipe: list):
    for i in range(len(equipe)):
        print(f"{i+1}: {equipe[i]}")


def ajouter_pokemon(equipe: list, *pokemon: str):
    for p in pokemon:
        equipe.append(p)
    return equipe
