def calcul_aire_rectangle(longueur, largeur):
    return longueur*largeur




def calcul_perimetre_rectangle(longueur, largeur):
    return 2*(longueur+largeur)

def main():
    longueur = int(input("Entrez la longueur du rectangle : "))
    largeur = int(input("Entrez la largeur du rectangle : "))
    print("L'aire du rectangle est : ", calcul_aire_rectangle(longueur, largeur))
    print("Le périmètre du rectangle est : ", calcul_aire_rectangle(longueur, largeur))