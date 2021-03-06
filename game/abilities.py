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
    AUXILLARY = 0
    ACTIVE = 1
    PASSIVE = 2

    # remember to update if you're updating this Type
    COUNT = 3

# Base class for defining an ability. Subclassed into active, passive and
# auxillary
class Ability():

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
            # outputted saying that we got extra/erroneous data. @TODO
            setattr(self, k, v)

    def __str__(self):
        txt = "Ability {0} has a cooldown of {1} secs and provides {2} effect(s)"
        return txt.format( self.name, self.cooldown, len(self.provides) )


# Active abilities can be used in a Rotation
class ActiveAbility(Ability):

    ability_range = 3


# Passive abilities, no activation - determine effectiveness of Rotation
# (and can potentially craft it, think EF)
class PassiveAbility(Ability):

    internal_cooldown = 1


# Maps the above enum to appropriate types
ATYPE_MAP = [ Ability,
              ActiveAbility,
              PassiveAbility ]


class AbilityList():

    def __init__(self):
        # Store the ability collections
        self.collections = []

        # Create collections for all the defined types
        for i in range(ABILITY_TYPE.COUNT):
            self.collections.append({})

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

                return False
        else:
            try:
                for key, ability in data.items():
                    # Built-in types only?;
                    try:
                        a = ATYPE_MAP[subtype](ability["name"])
                    except TypeError as e:
                        # @TODO use correct error outputting
                        print("subtype index is %s" % subtype)

                    # Populate the Abilities properties from the JSON data.
                    a.create(ability)

                    # Add the ability to the appropriate collection
                    self.add(a, subtype)

            except AttributeError as e:
                print("Invalid data passed, operation failed.")
                print("Error: {0} \n".format(e))
                print(data)

                return False

        return True


    def add(self, ability, subtype = None):
        # We trust subtype over the ability type because ability type may
        # be 'Ability' if there isn't any special properties that require
        # a new class (although this will probably change)
        if subtype is not None:
            self.collections[subtype].update({ability.name: ability})

        # Adds an ability to the list, using either the Type of the object
        # or the specific subtype, if defined.
        for i in range(ABILITY_TYPE.COUNT):
            if isinstance(ability, ATYPE_MAP[i]):
                self.collections[i].update({ability.name: ability})

    # This method could possibly lead to performance issues if we are constantly
    # looking up abilities. This is why it's so important to create smaller
    # lists for an avatar and potentially a better look-up table.
    def get(self, ability):
        for i in range(ABILITY_TYPE.COUNT):
            if ability in self.collections[i]:
                return self.collections[i][ability];
            else:
                # @TODO use correct error reporting facility and exit.
                print("Ability doesn't exist or is not loaded")


    # Return all abilities in this list
    def all(self):
        combined = dict()

        def merge(x, y):
            '''Given two dicts, merge them into a new dict as a shallow copy.'''
            z = x.copy()
            z.update(y)
            return z

        for i in range(ABILITY_TYPE.COUNT):

            combined = merge(self.collections[i], combined)

        return combined


class Deck(AbilityList):

    # @TODO this entire piece of code needs to be re-thought. Every time we do
    # anything to abilities we are doing them for both actives and passive.
    # Most of the time the behaviour is exactly the same - the only real difference
    # between the abilities is a) the number we can have of each and b) the way
    # they operate in combat. We should definitely keep two different classes
    # but they should all be in a single collection - even if we maintain seperate
    # lists of keys to access them quickly, rather than iterate through everytime
    # we want to access 'just the passives' or whatever.

    # Over-write this method adding in limitations such as max number of abilites
    # allowed in various subtypes
    def add(self, ability, subtype = None):
        # Adds an ability to the list, using either the Type of the object
        # or the specific subtype, if defined.
        if isinstance(ability, ActiveAbility) or subtype == ABILITY_TYPE.ACTIVE:
            if len(self.collections[ABILITY_TYPE.ACTIVE]) >= MAX_ACTIVES:
                #print("Active ability list full")
                return False
            else:
                # if there is already an elite, and this ability is an elite
                # then remove the former before adding
                if ability.is_elite and \
                    len(self.get_elite(ABILITY_TYPE.ACTIVE)) >= 1:
                    # remove the old elite
                    self.collections[ABILITY_TYPE.ACTIVE].pop(
                        self.get_elite(ABILITY_TYPE.ACTIVE)[0].name)

                self.collections[ABILITY_TYPE.ACTIVE].update(
                    {ability.name: ability})

                # check ability has been added to dictionary
                return ability.name in self.collections[ABILITY_TYPE.ACTIVE]
        elif isinstance(ability, PassiveAbility) or \
            subtype == ABILITY_TYPE.PASSIVE:
            if len(self.collections[ABILITY_TYPE.PASSIVE]) >= MAX_PASSIVES:
                #print("Passive ability list full")
                return False
            else:
                # if there is already an elite, and this ebility is an elite
                # then remove the former before adding
                if ability.is_elite and \
                    len(self.get_elite(ABILITY_TYPE.PASSIVE)) >= 1:
                    # remove the old elite
                    self.collections[ABILITY_TYPE.PASSIVE].pop(
                        self.get_elite(ABILITY_TYPE.PASSIVE)[0].name)

                self.collections[ABILITY_TYPE.PASSIVE].update(
                    {ability.name: ability})

                # check ability has been added to dictionary
                return ability.name in self.collections[ABILITY_TYPE.PASSIVE]


    # returns an ability or a list of abilities if there are multiple elites.
    # will search both actives and passives unless a specific type is specified.
    def get_elite(self, subtype = None):
        # define list to be returned
        _list = []

        # only iterate through lists once subtype is set.
        if subtype is not None:
            collection = self.collections[subtype]
            for k,a in collection.items():
                if a.is_elite:
                    _list.append(a)

        else:
            for subtype in xrange(ABILITY_TYPE.COUNT):
                _list += self.get_elite(subtype)

        return _list

import data
import game

class Wheel():
	# The Wheel class is a special ability list that is designed to hold the
	# entire list of abilities. We should also be building extra search and
	# cache functionality into the Wheel object as its primary function is to be
	# search through to find and match abilities to criteria. The base
	# AbilityList may not need this, and a Deck certainly doesn't, because the
	# amount of abilities is so small.
    def __init__(self):
        # Wheel object will be tightly coupled with the object that is loading
        # and storing game data.

        # The wheel is organised using the hierarchy: weapon > level (inner/outer)
        # and tree.
        # The Wheel object will hold several AbilityList objects, one for each tree
        # (the trees are defind by game data? or is that a property of the wheel?)
        self.trees = dict()

        # Each tree belongs to a weapon. If we take the trees and added them to
        # a weapon, then we can quickly cut down the number of trees we need to
        # search for a weapon.
        self.weapons = dict()

        for i in range(game.WEAPONS.COUNT):
            self.weapons.update({i: set()})

        # DataStore.get("abilities") <<< once implemented
        raw_data = data.load()
        actives = raw_data["actives"]
        passives = raw_data["passives"]

        # combine the dictionaries
        ability_data = {**actives, **passives}

        # Comb the data and create smaller collections for matching 'tree' name
        for k,a in ability_data.items():
            if not a["tree"] in self.trees.keys():
                # create a new tree
                self.trees.update({a["tree"]: AbilityList()})

                # attach the tree to a weapon's set.
                self.weapons[a["weapon"]].add(a["tree"])

            # Add ability to the tree.
            ability = ATYPE_MAP[a["category"]](a["name"])
            ability.create(a)

            self.trees[a["tree"]].add(ability)
