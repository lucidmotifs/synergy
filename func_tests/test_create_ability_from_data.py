# import modules
import data

# import classes
import game.abilities

# This test suite tests the ability to create Ability objects from raw
# data.

def run():
    test_data = data.load()[0].values()  # active abilities
    #print(data.abilities.load()[0].items())
    al = game.abilities.AbilityList()

    # loop through data creating an ability from each 'name'
    for ability in test_data:
        #print(ability["name"])
        if al.populate({'test_ability': ability}, "actives"):
            print("\nAdded: %s" % ability["name"])
            print()
            print("Print object: ")
            print(al.actives[-1])
            print()
        else:
            print("Failed!\n")
            # TODO Add debug info as to why this test failed.
            return 0

    return 1