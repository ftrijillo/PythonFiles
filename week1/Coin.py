from random import choices

class Coin(object):
    def __init__(self):
        self.side = 'heads'

    def flip(self):
        possibilities = ['heads', 'tails', 'off table', 'side']
        self.side = choices(possibilities, [100,100,30,2], k=10)

    def get_side(self):
        return self.side

c = Coin()
for i in range(10):
    c.flip()
    print(c.get_side())
