import abilities
import data.abilities

# This test suite tests the ability to create Ability objects from raw
# data.

def run():
    test_data = data.abilities.load()[0].values()  # active abilities
    print(data.abilities.load()[0].items())
    al = abilities.AbilityList()

    # loop through data creating an ability from each 'name'
    for ability in test_data:
        print(ability["name"])
        if al.add(ability):
            print("Added: %s" % ability["name"])
        else:
            print("Failed!")
            return 0

    return 1
