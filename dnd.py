# take a string representing a roll in D&D ("2d4+3" is two four sided dice with 3 added to the value at the end)
import re
import random

def dnd(roll):
    matches = re.match(r'(\d*)d(\d+)\+?(\d+)?', roll)
    num_dice = int(matches.group(1))
    num_sides = int(matches.group(2))
    off_set = int(matches.group(3)) or 0

    roll_value = 0
    for _ in range(num_dice):
        roll_value += random.randint(1, num_sides)
    roll_value += off_set
    return roll_value

def print_roll_multiple_times(roll, num_rolls):
    for _ in range(num_rolls):
        print(dnd(roll))



def test_dnd_out_of_bounds():
    roll = "2d5+1"
    for _ in range(100):
        if dnd(roll) > 11:
            return False
        if dnd(roll) < 3:
            return False
    return True


def test_dnd_reaches_extremes():
    roll = "2d5+1"
    reached_max = False
    reached_min = False
    for _ in range(10000000000):
        if dnd(roll) == 11:
            reached_max = True
        if dnd(roll) == 3:
            reached_min = True
        if reached_max and reached_min:
            return True
    return False


def tester():
    tests = [test_dnd_out_of_bounds, test_dnd_reaches_extremes]

    for test in tests:
        print(test.__name__ + ":")
        if test():
            print("Success")
        else:
            print("Failed")


tester()