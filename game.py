from player import Player
import random

class Game:
    def __init__(self, num_player: int):
        self.players_in = []
        self.players_out = []
        for i in range(num_player):
            self.players_in.append(Player(input(f'Enter name for player {i+1}: ')))
        
    
    def roll_dice(self, num_dice: int) -> list:
        """rolls the dice
        
        Args:
            num_dice (int): the number of dice to roll
        
        Returns:
            list: the dice rolls
        """
        rolls = []
        for i in range(num_dice):
            rolls.append(random.randint(1, 6))
        return rolls

    def _print_dice(self, dice: list):
        """prints the dice
        
        Args:
            dice (list): the dice to print
        """
        for i in range(len(dice)):
            print(f'{f"[{i+1}]: ":<4}{dice[i]:<4}', end='')
        print('')
    
    def take_turn(self, player: Player):
        """takes a turn for the player
        
        Args:
            player (Player): the player taking the turn
        """
        roll_i = 0
        roll_again = True
        kept_dice = []
        dice_to_roll = 5
        
        print(f'{f"----- {player.name} -----":^26}')
        while roll_i <= 3 and roll_again:
            rolls = self.roll_dice(dice_to_roll)
            roll_i += 1
            if kept_dice != []:
                print('Kept Dice:', end='')
                self._print_dice(kept_dice)
                'TODO: ask if the player wants to reroll dice'
            print(f'Roll {roll_i}:', end='')
            self._print_dice(rolls)
            
            
            if roll_i < 3:
                # check if player wants to keep any dice
                
                'TODO: loop over a copy of list, pop from original'
                nums = [int(n) for n in input("Which dice do you want to keep? \n(enter the numbers separated by spaces)\n").split()]
                i = 0
                for num in nums.copy():
                    kept_dice.append(rolls.pop(num-(1+i)))
                    dice_to_roll -= 1
                    i += 1
                
                # check if player wants to roll again
                valid = False
                while not valid:
                    match (input("do you want to roll again? (y/n): ")):
                        case 'y':
                            roll_again = True
                            valid = True
                        case 'n':
                            self.score(player, kept_dice+rolls)
                            return
                        case _:
                            print("Invalid input. Please enter 'y' or 'n'")
            else:
                self.score(player, kept_dice+rolls)
                        
    def score(self, player: Player, dice: list[int]):
        """scores the player's dice
        
        Args:
            player (Player): the player to score
        """
        pass