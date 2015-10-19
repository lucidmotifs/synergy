import game.abilities

dir(game)

# Player Class implementation
class Player:
    # stats object
    _stats = None
    # managed ability list
    _abilities = None
    # item list
    _items = None

    def __init__(self):
        self._stats = Stats()
        self._abilities = abilities.AbilityList()

    def add_ability(self, ability):
        


# Stats class implementation
# class hold each stat, as acts as a short-cut for calling
# game formulas that calculate certain RNG elements, given a particular
# stat point.
class Stats:
    # Base Stats - manually entered or derived from gear object.
    hit = 0
    penetration = 0
    critical = 0
    crit_power = 0

    def __init__(self):
        pass
