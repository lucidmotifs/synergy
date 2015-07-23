import os
import json

# Object that holds the data for abilitites.
# Auto loads its dictionary when initialized.
def load():
    actives = {}
    passives = {}
    auxillary = {}

    cwd = os.path.dirname(os.path.realpath(__file__))

    with open(cwd + '/active.json') as active_list:
        actives = json.load(active_list)
    with open(cwd + '/passive.json') as passive_list:
        passive = json.load(passive_list)

    loaded = [actives, passives]

    return loaded
