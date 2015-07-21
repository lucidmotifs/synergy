# abilities.py

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
    auxillary = Ability()

    def add(name):
        if name in data.abilities.active.values():
            actives.append(ActiveAbility(name))
        elif name in data.abilities.passive.values():
            passvies.append(ActiveAbility(name))
        elif name in data.abilities.aux.values():
            auxillary = Ability(name)

# Temporary script to define abilities (active and passive) that
# can be used for testing purposes.
# Final release should have all these definitions in XML/JSON files.

helter_skelter = ActiveAbility("Helter Skelter")
