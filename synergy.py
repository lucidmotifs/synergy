# system imports
import sys

# synergy imports
import abilities
import affects
import tests

# Entry point for the application

def main(args, kwargs):
    # run the application...
    # initially we want to display a menu with the potential options.

    # ideas for options:
    # - build an avatar (modify player object)
    # - run a test (opens new menu for tests built)
    # - create a build (modify an ability list)
    print("Welcome...S.Y.N.E.R.G.Y Online.")

    _opt = ''
    while not _opt == 'x' and not _opt == 'X':
        # Display menu
        print("Select from the options below:")
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

        _opt = 'x'

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
        print("Tests Menu:")
        print("-----------")
        print("Select from the options below:")
        print("==============================")
        print()
        print("(1) Test Thunderstruck vs Rapid Getaway")
        print()
        print("E(x)it the menu")
        print()

        _opt = input("Enter choice:")

        # capture the result of test
        result = 0
        if _opt == 1:
            # Execute a test case
            result = tests.thunderstruck_vs_rapidgetaway
        else if _opt == 'x' or _opt == 'X':
            print("Leaving menu...")
            print()
        else:
            print("Invalid selection, please choose a valid menu item.")
            print()


# boilerplate python to run main() when script is launched from console
if __name__ == "__main__":
	try:
		sys.exit( not main([],{}) )
	except KeyboardInterrupt:
		sys.exit( 1 )
