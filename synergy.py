# system imports
import sys

# synergy imports
import abilities
import affects

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

        _opt = 'x'

    return 0

# boilerplate python to run main() when script is launched from console
if __name__ == "__main__":
	try:
		sys.exit( not main([],{}) )
	except KeyboardInterrupt:
		sys.exit( 1 )
