# Test to ensure that the data imported via JSON is sane
# and useable by synergy objects.
import data.abilities

def run():
    test_data = data.abilities.Abilities()

    print("Number of Abilities Loaded: %s" % len(test_data.actives))
    print("Raw Data:")
    print(test_data.actives)

    print()
    print("Printing random ability name: ")
    print(test_data.actives["helter_skelter"]["name"])
    print()

    print()
    print("Display formatted provides tree: ")
    print()

    provides = test_data.actives['helter_skelter']['provides']

    for k,v in provides.items():
        print(k)
        print(v)

    print()

    return 1
