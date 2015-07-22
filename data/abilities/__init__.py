import os
import json
# Object that holds the data for abilitites.
# Auto loads its dictionary when initialized.
class Abilities():
    actives = {}
    passives = {}
    auxillary = {}

    def __init__(self):
        cwd = os.path.dirname(os.path.realpath(__file__))

        with open(cwd + '/active.json') as active_list:
            self.actives = json.load(active_list)
