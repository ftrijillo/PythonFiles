from random import choice

class Coin(object):
    def __init__(self):
        self.side = 'heads'

    def flip(self):
        possibilities = ['heads', 'tails']
        self.side = choice(possibilities)

    def get_side(self):
        return self.side


class Die(object):
    def __init__(self, max_side):
        self.side = 1
        self.max_side = max_side

    def roll(self):
        possibilities = range(1, self.max_side + 1)
        self.side = choice(possibilities)

    def get_side(self):
        return self.side

first_die = Die(6)
second_die = Die(6)
for i in range(1,10):
    first_die.roll()
    second_die.roll()
    print ("First Side: %s, Second Side: %s, Total: %s" % (first_die.get_side(), second_die.get_side(), first_die.get_side() + second_die.get_side()))
