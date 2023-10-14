#  Copyright (c) 2022. Code by Dimitri AIGLE

from random import randint

nbr_secret = randint(0,10)
nbr_of_try = 0

while True:
    try:
        nbr = int(input('rentrez un nombre > '))
        raise Exception('oops')
    # Quasiment toute les exception hérite de exception donc il y a un ordre !
    except ValueError:
        print("Vous devez rentrer un nombre")
    except Exception:
        print("oops !")
    else:
        if nbr == nbr_secret:
            print("bravo 🏆")
            break
        elif nbr > nbr_secret:
            print("le nombre est plus petit ")
        else :
            print("le nombre est plus grand")
    finally:
        nbr_of_try += 1
        print(nbr_of_try)

