# import modules
import data

# import classes
from game.abilities import AbilityList
from game.abilities import Wheel
from game.abilities import ABILITY_TYPE

# This test suite tests the ability to create the Wheel object from raw
# data.

def run():
    wheel = Wheel()

    # Check collections
    print("Trees currently loaded into the wheel\n")
    for tree_name in wheel.trees.key():
        print(tree_name + "\n")
