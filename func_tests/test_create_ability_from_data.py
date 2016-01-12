# import modules
import data

# import classes
from game.abilities import AbilityList

# This test suite tests the ability to create Ability objects from raw
# data.

def run():
	test_data = data.load()["actives"].values()  # active abilities

	# fail test if test_data is empty
	if test_data is None:
		print ("Fail: No test data loaded")
		return 0

	al = AbilityList()

	# loop through data creating an ability from each 'name'
	for ability in test_data:
		#print(ability["name"])
		if al.populate({'test_ability': ability}, "actives"):
			print("\nAdded: %s" % ability["name"])
			print()
			print("Print object: \n")
			try:
				print(al.actives[ability["name"]])
			except KeyError:
				print("Invalid data, printing debug info...")
				print(al.actives)
			print()
		else:
			print("Failed!\n")
			# TODO Add debug info as to why this test failed.
			return 0

	return 1
