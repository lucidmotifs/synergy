# abilities.py
from . import affects
import data

# constants
MAX_ACTIVES = 7
MAX_PASSIVES = 7
MAX_ACTIVE_AUXILLARY = 1
MAX_PASSIVE_AUXILLARY = 1

# struct for trying to decouple the active/passive behaviour somewhat
class ABILITY_TYPE:
    ACTIVE = 1
    PASSIVE = 2
    AXUILLARY = 3

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

    # @TODO this entire piece of code needs to be re-though. Every time we do
    # anything to abilities we are doing them for both actives and passive.
    # Most of the time the behaviour is exactly the same - the only real difference
    # between the abilities is a) the number we can have of each and b) the way
    # they operate in combat. We should definitely keep two different classes
    # but they should all be in a single collection - even if we maintain seperate
    # lists of keys to access them quickly, rather than iterate through everytime
    # we want to acces 'just the passives' or whatever.

    # Over-write this method adding in limitations such as max number of abilites
    # allowed in various subtypes
    def add(self, ability, subtype = None):
        # Adds an ability to the list, using either the Type of the object
        # or the specific subtype, if defined.
        if isinstance(ability, ActiveAbility) or subtype == 'active':
            if len(self.actives) >= MAX_ACTIVES:
                #print("Active ability list full")
                return False
            else:
                # if there is already an elite, and this ebility is an elite
                # then remove the former before adding
                if len(self.get_elite("actives") >= 1) && ability.is_elite:
                    # remove the old elite
                    self.actives.pop(self.get_elite("actives")[0].name)

                self.actives.update({ability.name: ability})
                # check ability has been added to dictionary
                return ability.name in self.actives
        elif isinstance(ability, PassiveAbility) or subtype == 'passive':
            if len(self.passives) >= MAX_PASSIVES:
                #print("Passive ability list full")
                return False
            else:
                # if there is already an elite, and this ebility is an elite
                # then remove the former before adding
                if len(self.get_elite("passvies") >= 1) && ability.is_elite:
                    # remove the old elite
                    self.passives.pop(self.get_elite("passives")[0].name)

                self.passives.update({ability.name: ability})
                # check ability has been added to dictionary
                return ability.name in self.passives


    # returns an ability or a list of abilities if there are multiple elites.
    # will search both actives and passives unless a specific type is specified.
    def get_elite(self, subtype = None):
        # define list to be returned
        _list = []

        # only iterate through lists once subtype is set.
        if subtype is not None:
            if subtype == "actives":
                for a in self.actives:
                    if a.is_elite:
                        _list.append(a)
            else if subtype == "passives":
                for a in self.passives:
                    if a.is_elite:
                        _list.append(a)

        else:
            for subtype in ("actives", "passives"):
                _list += self.get_elite(subtype)
