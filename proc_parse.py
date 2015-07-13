# Script to determine optimal damage output for procs
# Initially crit and pen % will have to be manually entered.
# In future, hopefully this module can be used with just crit/pen glyph
# points (plus minor crit / major crit chance)

# Define proc damage. Should be related to Attack Power - TODO fine formula
class PROCS:
    ONE_IN_THE_CHAMBER = 264
    SUDDEN_RETURN = 264
    THUNDERSTRUCK = 394


def test_thunderstruck_vs_rapidgetaway():
    # test at different crit %
    crit_chance = 20
    # assume 1000dps (test scaling DPS later)
    dps = 1000
    # This test is to see whether more damage is gained
    # from which elite passive.

    # combat in 10 seconds (approx single round)
    base_dmg = 10 * dps
    crit_dmg = base_dmg * (crit_chance / 100)
