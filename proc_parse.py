# Script to determine optimal damage output for procs
# Initially crit and pen % will have to be manually entered.
# In future, hopefully this module can be used with just crit/pen glyph
# points (plus minor crit / major crit chance)

# Define proc damage. Should be related to Attack Power - TODO find formula
class PROCS:
    ONE_IN_THE_CHAMBER = 264
    SUDDEN_RETURN = 264
    THUNDERSTRUCK = 392

# This test is to see whether more damage is gained
# from which elite passive.
def test_compare_elite_passives(this, that):
    ## Set All variables TODO make external variables

    # test at different crit %
    crit_chance = 20
    # assume 1000dps (test scaling DPS later)
    dps = 1000
    # laceration signet
    have_laceration = True
    # have THUNDERSTRUCK
    using_thunderstruck = this
    # have rapid getaway
    using_rapidgetaway = that
    # have one in the chamber
    using_oneinthechamber = False


    # combat in 10 seconds (approx single round)
    base_dmg = 10 * dps
    base_crit = crit_chance  # percent
    if using_rapidgetaway:
        base_crit += 10
    base_crit_dmg = .4

    # with laceration signet
    if have_laceration:
        base_crit_dmg += .24

    # assume no randomness over 10 hits
    dmg_per_hit = dps

    crits_per_round = base_crit / 10  # (15/100)*10
    crit_hit_dmg = dmg_per_hit * (1 + base_crit_dmg)
    # builder dmg needs to be seperated from consumer (crit % will differ too...)
    crit_dmg = base_dmg * (crit_chance / 100)

    crit_dmg_per_round = crit_hit_dmg * crits_per_round

    proc_dmg_per_crit = 0
    if using_oneinthechamber:
        proc_dmg_per_crit += PROCS.ONE_IN_THE_CHAMBER  # ONE_IN_THE_CHAMBER
    if using_thunderstruck:
        proc_dmg_per_crit += PROCS.THUNDERSTRUCK

    proc_dmg_per_round = proc_dmg_per_crit * crits_per_round

    print("Base Damage: %d \n" % base_dmg)
    print("Crit Damage: {0} ({1}% Crit) \n".format(int(crit_dmg_per_round), base_crit))
    print("Proc Damage: %d \n" % proc_dmg_per_round)

    return base_dmg + crit_dmg_per_round + proc_dmg_per_round


print(test_compare_elite_passives(True, False))
print(test_compare_elite_passives(False, True))
