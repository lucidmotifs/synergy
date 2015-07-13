# Base Class Definitions
class Affect:

    duration = 0

    def __init__(self):
        # not implemented
        pass

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

    def provide():
        pass


class ActiveAbility(Ability):

    ability_range = 0


class PassiveAbility(Ability):

    internal_cooldown = 0
