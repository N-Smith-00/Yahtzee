from player import Player

class Game:
    def __init__(self, num_player: int):
        self.players = []
        for i in range(num_player):
            self.players.append(Player(input(f'Enter name for player {i+1}: ')))
        print([player.name for player in self.players])
        input()