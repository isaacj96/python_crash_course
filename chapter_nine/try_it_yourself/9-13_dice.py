import random


class Dice:
    """Represent a dice that can be rolled."""

    def __init__(self, sides=6):
        """initialize the Dice to have 6 sides as default but can change"""
        self.sides = sides

    def roll_die(self):
        """Roll the dice by calling the randint function"""
        return random.randint(1, self.sides)


my_dice = Dice(20)

x = 10
i = 0
while i < x:
    print(my_dice.roll_die())
    i += 1
