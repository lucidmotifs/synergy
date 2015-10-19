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
