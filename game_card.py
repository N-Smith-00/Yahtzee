class GameCard:
    def __init__(self):
        # upper section
        self.ones = None
        self.twos = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None
        self.upper_sec = (self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes)

        # upper section
        self.three_kind = None
        self.four_kind = None
        self.full_house = None
        self.sm_strt = None
        self.lg_strt = None
        self.yahtzee = None
        self.yahtzee_bonus = 0
        self.chance = None
        self.lower_sec = (self.three_kind, self.four_kind, self.full_house, self.sm_strt, self.lg_strt, self.yahtzee, self.chance)

        self.grand_total = 0
    
    def _sum_upper(self) -> int:
        """calculates the total of the upper section

        Returns:
            int: the total of the upper section
        """
        total = 0
        for entry in self.upper_sec:
            if entry != None:
                total += entry
        return total
    
    def _sum_lower(self) -> int:
        """calculates the total of the lower section

        Returns:
            int: the total of the lower section
        """
        total = self.yahtzee_bonus*100
        for entry in self.lower_sec:
            if entry != None:
                total += entry
        return total
    
    def __str__(self) -> str:
        return f'''|--------------------------|
|{'Score Card':^26}|
|{' '*26}|
|--------------------------|
|{'Upper Section':^26}|
|{'Ones:':>13}{self.ones if self.ones != None else '':^13}|
|{'Twos:':>13}{self.twos if self.twos != None else '':^13}|
|{'Threes:':>13}{self.threes if self.threes != None else '':^13}|
|{'Fours:':>13}{self.fours if self.fours != None else '':^13}|
|{'Fives:':>13}{self.fives if self.fives != None else '':^13}|
|{'Sixes:':>13}{self.sixes if self.sixes != None else '':^13}|
|{'Upper Total:':>13}{self._sum_upper():^13}|
|--------------------------|
|{'Lower Section':^26}|
|{'3 of a Kind:':>13}{self.three_kind if self.three_kind != None else '':^13}|
|{'4 of a Kind:':>13}{self.four_kind if self.four_kind != None else '':^13}|
|{'Full House:':>13}{self.full_house if self.full_house != None else '':^13}|
|{'Sm. Straight:':>13}{self.sm_strt if self.sm_strt != None else '':^13}|
|{'Lg. Straight:':>13}{self.lg_strt if self.lg_strt != None else '':^13}|
|{'Yahtzee:':>13}{self.yahtzee if self.yahtzee != None else '':^13}|
|{'Chance:':>13}{self.chance if self.chance != None else '':^13}|
|{'Yahtzee':>12}{'X'*self.yahtzee_bonus:>6}{'':^8}|
|{'Bonus:':>13}{self.yahtzee_bonus*100 if self.yahtzee_bonus>0 else '':^13}|
|{'Lower Total:':>13}{self._sum_lower():^13}|
|{'Upper Total:':>13}{self._sum_upper():^13}|
|{'Grand Total:':>13}{self._sum_upper() + self._sum_lower():^13}|
|--------------------------|'''