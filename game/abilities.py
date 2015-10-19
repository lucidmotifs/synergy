# abilities.py
from . import affects
import data

# constants
MAX_ACTIVES = 7
MAX_PASSIVES = 7
MAX_ACTIVE_AUXILLARY = 1
MAX_PASSIVE_AUXILLARY = 1

# Base class for defining an ability. Subclassed into active, passive and
# auxillary
class Ability:

    name = ""

    provides = ()
    requires = ()

    cooldown = 0

    is_elite = 0
    is_auxillary = 0

    def __init__(self, name):
        self.name = name

    def create(self, raw):
        for k,v in raw.items():
            # Lazy object creation. Let's check if we HAVE the attribute
            # and if we do, then set it. If we don't, we want a debug message
            # outputted saying that we got extra/erroneous data.
            setattr(self, k, v)

    def __str__(self):
        return "Ability {0} has a cooldown of {1} secs and has {2} provides".format(
        self.name,
        self.cooldown,
        len(self.provides))


# Active abilities can be used in a Rotation
class ActiveAbility(Ability):

    ability_range = 3


# Passive abilities, no activation - determine effectiveness of Rotation
# (and can potentially craft it, think EF)
class PassiveAbility(Ability):

    internal_cooldown = 1


class AbilityList():

    actives = {}
    passives = {}
    auxillary = None

    # Fill the list with a pre-defined set of objects from a dictionary.
    # This is generally used to create the ability wheel from game data,
    # but can also be used as an import/export feature.
    def populate(self, data, subtype = None):
        if not subtype:
            try:
                for key, value in data.items():
                    # key is subtype, value is data
                    # ensure we don't pass a key of 'None' or will
                    # loop forever (maybe?)
                    if key is not None:
                        self.populate(value, key)
                    else:
                        return False
            except ValueError as e:
                print("Invalid data passed, populate operation failed.")
                print("Error: {0} on data supplied \n {1}".format(e, data))
        else:
            try:
                for key, value in data.items():
                    # debugging
                    print (value)
                    if subtype == "actives":
                        a = ActiveAbility(value["name"])
                    elif subtype == "passives":
                        a = PassiveAbility(value["name"])
                    else:
                        a = Ability(value["name"])

                    # Populate the Abilities properties from the JSON data.
                    a.create(value)
                    self.add(a, subtype)

            except AttributeError as e:
                print("Invalid data passed, operation failed.")
                print("Error: {0} \n".format(e))
                print(data)

        return len(self.actives) or len(self.passives)


    def add(self, ability, subtype = None):
        # Adds an ability to the list, using either the Type of the object
        # or the specific subtype, if defined.
        if isinstance(ability, ActiveAbility) or subtype == 'active':
            self.actives.update({ability.name: ability})
        elif isinstance(ability, PassiveAbility) or subtype == 'passive':
            self.passives.update({ability.name: ability})

    # This method could possibly lead to performance issues if we are constantly
    # looking up abilities. This is why it's so important to create smaller
    # lists for an avatar and potentially a better look-up table.
    def get(self, ability):
        if ability in self.actives:
            return self.actives[ability];
        elif ability in self.passives:
            return self.passives[ability];


class Deck(AbilityList):

    # Over-write this method adding in limitations such as max number of abilites
    # allowed in various subtypes
    def add(self, ability, subtype = None):
        # Adds an ability to the list, using either the Type of the object
        # or the specific subtype, if defined.
        if isinstance(ability, ActiveAbility) or subtype == 'active':
            if len(self.actives >= MAX_ACTIVES):
                #print("Active ability list full")
                return False
            else:
                self.actives.update({ability.name: ability})
                # check ability has been added to dictionary
                return ability.name in self.actives
        elif isinstance(ability, PassiveAbility) or subtype == 'passive':
            if len(self.passives >= MAX_PASSIVES):
                #print("Passive ability list full")
                return False
            else:
                self.passives.update({ability.name: ability})
                # check ability has been added to dictionary
                return ability.name in self.passives
