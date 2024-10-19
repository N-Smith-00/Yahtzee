from game_card import GameCard

def main():
    # intro and main menu
    print('Welcome to Yahtzee!')
    input('Press Enter to start...')
    menu()

def menu():
    # main menu
    print(f'{'Yahtzee':^26}')
    print(f'{'1. Play Game':<26}')
    print(f'{'2. Rules':<26}')
    print(f'{'3. Quit':<26}')
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
            print('Invalid choice. Try again.')
            menu()

def game():
    # play game
    pass

def rules():
    # display rules
    pass

main()