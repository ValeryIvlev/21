import random


def give_me_number():
    return random.randint(6, 11)


def start_game():
    print('-'*23, 'Добро пожаловать в игру', '-'*23, sep='\n')
    print('hit  | Бросить кости', 'hold | Остановиться', '-'*23, sep='\n')

def game():
    start_game()
    player_score = 0
    diller_score = 0
    a = input().lower()
    while a == 'hit':
        player_score += give_me_number()
        print(f'Счет игрока = {player_score}')
        if player_score > 21:
            print('Игрок перебрал, Диллер выиграл')
            break
        elif player_score == 21:
            print('Игрок выиграл!')
            break

        print('-' * 23, 'hit  | Бросить кости', 'hold | Остановиться', '-' * 23, sep='\n')
        a = input().lower()

    while a == 'hold':
        if diller_score <= 16:
            diller_score += give_me_number()
            print(f'Счет диллера = {diller_score}')
        elif 16 <= diller_score <= 21:
            if player_score > diller_score:
                print(f'Игрок выиграл {player_score}, Диллер проиграл {diller_score}')
                break
            elif player_score == diller_score:
                print(f'Ничья! {player_score} = {diller_score}')
                break
            else:
                print(f'Диллер выиграл {diller_score}, Игрок проиграл {player_score}')
                break
        else:
            print("Диллер перебрал, игрок выиграл")
            break


game()