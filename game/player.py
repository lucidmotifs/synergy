from game.abilities import Deck

# Player Class implementation
class Player:
    # stats object
    _stats = None
    # managed ability list
    _deck = None
    # item collection - sorted/managed
    _items = None
    # signets collection
    _signets = None

    def __init__(self):
        self._stats = Stats()
        self._deck = Deck()


    # return the Deck the player is using.
    def deck(self):
        return self._deck


    # return the player stats object
    def stats(self):
        # TODO: implement
        return None


    # return the signets object if no arg provided, return the existence of
    # a particular signet if a string arg provided
    def signets(self, name = None):
        # TODO: implement
        return False


    # use deck/stats/signets - etc. to return a theorectical DPS value
    def base_tdps(self):
        # TODO: implement
        return 0


    # convience method to find if the player has a particular ability in their deck.
    def using_ability(self, name):
        return name in self.deck().actives or name in self.deck().passives



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
