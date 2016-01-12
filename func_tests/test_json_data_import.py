# Test to ensure that the data imported via JSON is sane
# and useable by synergy objects.
import data

def run():
	# List of all abilities
	test_data = data.load()

	# For each list in the test_data loaded.
	for d in test_data.values():
		# turn each result into a list
		l = list(d.values())

		print("Number of Abilities Loaded: %s" % len(l))
		print()
		print("Raw Data: \n")
		print(d.values())

		print()
		print("Printing random ability name: \n")
		print(l[0]["name"])
		print()

		try:
			provides = l[0]['provides']
			for k,v in provides.items():
				print("\nDisplay formatted provides tree: \n")
				print(k)
				print(v)
				print()
		except KeyError as e:
			print("Fail: Ability selected does not have a provides attribute")

	# line for readibility
	print()

	return 1  # pass
