import json
# Object that holds the data for abilitites.
# Auto loads its dictionary when initialized.
class Abilities():
    active = {}
    passive = {}
    auxillary = {}

    def __init__(self):
        with open('active.json') as active_list:
            active = json.load(active_list)
