import time
from game_card import GameCard
from game import Game

def main():
    menu()

def menu():
    # main menu
    print(f'{"----- Yahtzee -----":^26}')
    while True:
        print(f'{"----- Main Menu -----":^26}')
        print(f'{"1. Play Game":<26}')
        print(f'{"2. Rules":<26}')
        print(f'{"3. Quit":<26}')
        choice = input('Enter choice: ')
        match choice:
            case '1':
                game()
            case '2':
                rules()
            case '3':
                print('Goodbye!')
                exit()
            case _:
                print('\nInvalid choice. Try again.')
def game():
    # play game
    while True:
        num_players = input('Enter number of players: ')
        if num_players.isdigit():
            break
        else:
            print('Invalid input. Try again.')
    game = Game(int(num_players))
    
    playing = True
    while playing:
        for player in game.players_in:
            game.take_turn(player)
    

def rules():
    # display rules
    pass

if __name__ == "__main__":
    main()