from player import Player
import random

class Game:
    def __init__(self, num_player: int):
        self.players = []
        for i in range(num_player):
            self.players.append(Player(input(f'Enter name for player {i+1}: ')))
    
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
            print(f'{f"[{i+1}]: ":<8}{dice[i]:<8}')
    
    def take_turn(self, player: Player):
        """takes a turn for the player
        
        Args:
            player (Player): the player taking the turn
        """
        print(f'{f'----- {player.name}\'s turn -----':^26}')
        rolls = self.roll_dice(5)
        print(f'{player.name} rolled')
        self._print_dice(rolls)