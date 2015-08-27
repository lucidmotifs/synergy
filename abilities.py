# abilities.py
import affects
import data.abilities

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
            for key, value in data:
                # key is subtype, value is data
                return self.populate(value, key)
        else:
            for key, value in data.items():
                if subtype == "actives":
                    a = ActiveAbility(value["name"])
                elif subtype == "passives":
                    a = PassiveAbility(value["name"])
                else:
                    a = Ability(value["name"])
            # Populate the Abilities properties from the JSON data.
            a.create(value)
            self.add(a)

        return len(self.actives) or len(self.passives)


    def add(self, ability, subtype = None):
        # Adds an ability to the list, using either the Type of the object
        # or the specific subtype, if defined.
        if isinstance(ability, ActiveAbility) or subtype == 'active':
            self.actives.update({ability.name: ability})
        elif isinstance(ability, PassiveAbility) or subtype == 'passive':
            self.passives.append({ability.name: ability})

    # This method could possibly lead to performance issues if we are constantly
    # looking up abilities. This is why it's so important to create smaller
    # lists for an avatar and potentially a better look-up table.
    def get(self, ability):
        if ability in self.actives:
            return self.actives[ability];
        else if ability in self.passives:
            return self.passives[ability];

# Temporary script to define abilities (active and passive) that
# can be used for testing purposes.
# Final release should have all these definitions in XML/JSON files.

helter_skelter = ActiveAbility("Helter Skelter")
