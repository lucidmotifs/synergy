from player.stats import Stats
import abilities

dir(abilities)
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
        #self._abilities = abilities.AbilityList()
