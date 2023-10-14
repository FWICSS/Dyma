import random

def select_secret_word(words):
    words_list = words.split()
    secret = random.randint(0, len(words_list) - 1)
    return words_list[secret]

def update_game_state(game, letter):
    if letter.isalpha() and len(letter) == 1:
        game['guessed_letters'].add(letter)
        if letter in game['secret_word']:
            guess_word_list = list(game['guess_word'])
            for index, current_letter in enumerate(game['secret_word']):
                if current_letter == letter:
                    guess_word_list[index * 2] = letter
            game['guess_word'] = ''.join(guess_word_list)
        else:
            game['life'] -= 1

def print_game_state(game):
    print('Vies restantes :', game['life'])
    print('Lettres déjà essayées :', game['guessed_letters'])
    print('Mot à deviner :', game['guess_word'])

def game_over_condition(game):
    if '_' not in game['guess_word']:
        return 'Gagné'
    elif game['life'] < 1:
        return 'Perdu'
    return None

def play_one_round(game, letter):
    update_game_state(game, letter)
    return game_over_condition(game)

# Fonction principale pour jouer au jeu (peut être appelée dans le script principal)
def play_game():
    words = "abuser crottes fleches continental babiole etoile bougie coup coeur malade"
    in_game = True

    while in_game:
        secret_word = select_secret_word(words)
        game = {
            'secret_word': secret_word,
            'guess_word': '_ ' * len(secret_word),
            'life': 9,
            'guessed_letters': set()
        }

        while True:
            letter = input('Entrez une lettre : ')
            result = play_one_round(game, letter)
            print_game_state(game)

            if result == 'Gagné':
                print('Gagné !')
                replay = input('Rejouer ? (y/Y/O/o) : ')
                if replay not in ['y', 'Y', 'O', 'o']:
                    in_game = False
                break
            elif result == 'Perdu':
                print('Perdu !')
                replay = input('Rejouer ? (y/Y/O/o) : ')
                if replay not in ['y', 'Y', 'O', 'o']:
                    in_game = False
                break

if __name__ == '__main__':
    play_game()