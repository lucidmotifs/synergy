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

    return 0

# boilerplate python to run main() when script is launched from console
if __name__ == "__main__":
	try:
		sys.exit( not main([],{}) )
	except KeyboardInterrupt:
		sys.exit( 1 )
