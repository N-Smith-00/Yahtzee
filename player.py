from game_card import GameCard

class Player:
    def __init__(self, name: str):
        self.scorecard = GameCard()
        self.name = name