# affects.py
# All the various affects that can be applied. Including CC states and damage.
import synergy

class Affect:

    # Specific type related to the pertitent STRUCT
    subtype = 0
    # Shared properties between affects
    duration = 0

    def __init__(self, subtype = 0):
        self.subtype = subtype


class STATES:
    NONE = 0
    AFFLICTED = 1
    HINDERED = 2
    IMPAIRED = 3
    WEAKENED = 4


class State(Affect):

    label = None
    can_remove = False
    stack_count = 0
    intensity = 0

    # increase intensity/stacks of state
    def applyStack(num=1):
        self.stack_count += num


class BENEFITS:
    NONE = 0
    PENETRATION = 1
    CRITICAL = 2
    HIT = 3


class Benefit(Affect):

    magnitude = 0  # 1 is minor, 2 is major

    def getPercent():
        if self.subtype == 1:
            # penetration
            if magnitude == 1:
                return 15
            elif magnitude == 2:
                return 45
        elif self.subtype == 2:
            # critical
            if magnitude == 1:
                return 10
            elif magnitude == 2:
                # no such thing, potentially EF?
                return 100
        elif self.subtype == 3:
            # hit
            if magnitude == 1:
                return 10
            elif magnitude == 2:
                return 50
        else:
            return 0


class DAMAGES:
    NONE = 0
    DIRECT = 1
    PERIODIC = 2
    AREA = 3
