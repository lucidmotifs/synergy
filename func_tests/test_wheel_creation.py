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

    for tree_name in wheel.trees.keys():
        print(tree_name)
        print(wheel.trees[tree_name].collections[1])
        print(len(wheel.trees))
        print("Abilities:")

        for key,ability in wheel.trees[tree_name].all().items():
            print(str(tree_name) + "\t" + str(ability))
