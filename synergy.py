# system imports
import sys

# synergy imports
import game
import game.abilities
import game.affects
import func_tests
from func_tests import *

# class import
from game.abilities import AbilityList

# Entry point for the application

def main(args = [], kwargs = {}):
    # run the application...
    # initially we want to display a menu with the potential options.

    # ideas for options:
    # - build an avatar (modify player object)
    # - run a test (opens new menu for tests built)
    # - create a build (modify an ability list)
    print("\nWelcome...S.Y.N.E.R.G.Y Online.")

    _opt = ''
    while not _opt == 'x' and not _opt == 'X':
        # Display menu
        print("\nSelect from the options below:")
        print("==============================")
        print()
        print("(B)uild an Avatar. Modify your player object for use in tests")
        print("(R)un a Test. Select from a list of tests to run")
        print("(C)reate a Build. Create/Modify an Ability list")
        print()
        print("E(x)it the program")
        print()

        _opt = input("Enter choice: ")

        print("Your choice was {0}".format(_opt))

        if _opt == 'r' or _opt == 'R':
            # Tests menu
            display_tests_menu()

        else:
            print("Invalid option supplied, please enter only a valid menu key")

    return 0

# Althoug the below function may suffice for the moment, the correct way to
# implement console UI would be something like menus.<menu_name>.display()
# i.e. menus.tests.display()
# This way we can add options and have those options auto-run some
# definition.
def display_tests_menu():
    _opt = ''
    while not _opt == 'x' and not _opt == 'X':
        # Display menu
        print("\nTests Menu:")
        print("-----------")
        print("Select from the options below:")
        print("==============================")
        print()
        print("(1) Test Thunderstruck vs Rapid Getaway")
        print("(2) Test JSON Data Import")
        print("(3) Test Ability Object Creation")
        print()
        print("E(x)it the menu")
        print()

        _opt = input("Enter choice: ")

        print()

        # capture the result of test
        result = 0
        if _opt == "1":
            # Execute a test case
            al = ("Thunderstruck", "Rapid Getaway")
            result = test_compare_elite_passives.run(al)
        elif _opt == "2":
            # Execute a test case
            result = test_json_data_import.run()
        elif _opt == "3":
            # Execute a test case
            result = test_create_ability_from_data.run()
        elif _opt == 'x' or _opt == 'X':
            print("Leaving menu...")
            print()
            return main([], {})
        else:
            print("Invalid selection, please choose a valid menu item.")
            print()


# boilerplate python to run main() when script is launched from console
if __name__ == "__main__":
	try:
		sys.exit( not main([],{}) )
	except KeyboardInterrupt:
		sys.exit( 1 )
