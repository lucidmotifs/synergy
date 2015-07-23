# abilities.py
import affects
import data.abilities

# Base class for defining an ability. Subclassed into active, passive and
# auxillary
class Ability:

    name = ""

    provides = None
    requires = None

    cooldown = 0

    is_elite = 0
    is_auxillary = 0

    def __init__(self, name):
        self.name = name

    def requires():
        pass

    def provides():
        pass

# Active abilities can be used in a Rotation
class ActiveAbility(Ability):

    ability_range = 3

# Passive abilities, no activation - determine effectiveness of Rotation
# (and can potentially craft it, think EF)
class PassiveAbility(Ability):

    internal_cooldown = 1


class AbilityList():

    actives = []
    passives = []
    auxillary = None

    def add(self, name):
        if name in data.abilities.load()[0].values():
            self.actives.append(ActiveAbility(name))
            return True
        elif name in data.abilities.load()[1].values():
            self.passvies.append(PassiveAbility(name))
            return True
        elif name in data.abilities.load()[2].values():
            self.auxillary = Ability(name)
            return True
        else:
            return False

# Temporary script to define abilities (active and passive) that
# can be used for testing purposes.
# Final release should have all these definitions in XML/JSON files.

helter_skelter = ActiveAbility("Helter Skelter")
