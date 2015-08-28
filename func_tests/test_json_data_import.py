# Test to ensure that the data imported via JSON is sane
# and useable by synergy objects.
import data

def run():
    # List of all abilities
    test_data = data.load()

    # For each list in the test_data loaded.
    for d in test_data:
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

        print()
        print("Display formatted provides tree: ")
        print()

        provides = l[0]['provides']

        for k,v in provides.items():
            print(k)
            print(v)
            print()

    # line for readibility
    print()

    return 1  # pass
