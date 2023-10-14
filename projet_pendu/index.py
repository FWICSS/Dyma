import random
from randomwordfr import RandomWordFr

in_game = True
while in_game:

    rw = RandomWordFr()
    result = rw.get()
    secret_word = result['word']
    game = {
        "secret_word": secret_word,
        "guess_words": "_" * len(secret_word),
        "life": 9,
        "guess_letters": set()
    }


    def __game__():
        print(f"""
    ***************************************************************
    {game['guess_words']} | vie : {game['life']} 
    lettres essayé : {game['guess_letters']}
    ***************************************************************
    """)


    print(f"""
    ****************************************
    N O U V E L L E   P A R T I E  P E N D U
    
    {game['guess_words']} | vies : {game['life']}
    ****************************************
    """)
    while True:
        a = input('Entrez la lettre : ')
        if a == '' or a.isnumeric() or len(a) != 1:
            print("lettre nom entrez ou valeur numérique")
            pass
        elif a in secret_word and a not in game["guess_words"]:
            game['guess_letters'].add(a)
            print(f" Bravo {a} fait parti du mot")
            guess_word_list = list(game['guess_words'])
            for index, letter in enumerate(game['secret_word']):
                if letter == a:
                    guess_word_list[index] = a
            game["guess_words"] = "".join(guess_word_list)
            __game__()
        elif a not in secret_word:
            game['guess_letters'].add(a)
            game["life"] -= 1
            print(f" {a} ne fait pas parti du mot 💔")
            __game__()
        if game["guess_words"] == secret_word:
            print("You win ! 🏆")
            replay = input(f"""
                        *****************
                        You want replay ? (y/Y/yes/Yes/O)
                        *****************
                        """)
            if replay not in ['y', 'Y', "yes", "Yes", "O"]:
                in_game = False
            break
        elif game["life"] < 1:
            print(f"You lose ❌  | the word was {secret_word}")
            print(result['definition'])
            replay = input(f"""
            *****************
            You want replay ? (y/Y/yes/Yes/O)
            *****************
            """)
            if replay not in ['y', 'Y',"yes","Yes","O"]:
                in_game = False
            break


    match a:
        case "y" | "yes" | "oui":
            in_game = True
        case _:
            print("See you soon !")
