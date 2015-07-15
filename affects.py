# affects.py
# All the various affects that can be applied. Including CC states and damage.
import synergy

class Affect:

    duration = 0

    def __init__(self):
        # not implemented
        pass


class STATE_TYPES:
    NONE = 0
    AFFLICTED = 1
    HINDERED = 2
    IMPAIRED = 3
    WEAKENED = 4


class State(Affect):

    state_type = 0

    def __init__(self, stype):
        self.state_type = stype


class BENEFIT_TYPES:
    NONE = 0
    PENETRATION = 1
    CRITICAL = 2
    HIT = 3


class Benefit(Affect):

    benefit_type = 0
    magnitude = 0  # 1 is minor, 2 is major

    def __init__(self, btype):
        self.benefit_type = btype
