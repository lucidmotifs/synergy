# Test to ensure that the data imported via JSON is sane
# and useable by synergy objects.
import data.abilities

def run():
    test_data = data.abilities.load()[0]

    print("Number of Abilities Loaded: %s" % len(test_data))
    print("Raw Data:")
    print(test_data)

    print()
    print("Printing random ability name: ")
    print(test_data["helter_skelter"]["name"])
    print()

    print()
    print("Display formatted provides tree: ")
    print()

    provides = test_data['helter_skelter']['provides']

    for k,v in provides.items():
        print(k)
        print(v)

    print()

    return 1
