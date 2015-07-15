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
    ## Set All variables @TODO make external variables

    

    # Calculate avg damage per hit
    # Below values are at 2800 AR / 446 WP
    builder = 214
    consumer1 = 757
    consumer2 = 1511
    consumer_avg = (consumer1 + consumer2) / 2
    combat_time = 14

    consumers = combat_time / 7
    builders = combat_time - consumers

    base_damage = (builders * builder) + (consumers * consumer_avg)

    # test at different crit %
    crit_chance = 20
    # assume 1000dps (test scaling DPS later)
    dps = base_damage / combat_time
    # laceration signet
    have_laceration = True
    # have THUNDERSTRUCK
    using_thunderstruck = this
    # have rapid getaway
    using_rapidgetaway = that
    # have one in the chamber
    using_oneinthechamber = True


    # combat in 14 seconds (approx single round)
    base_dmg = base_damage
    base_crit = crit_chance  # percent
    if using_rapidgetaway:
        base_crit += 10
    base_crit_dmg = .4

    # with laceration signet
    if have_laceration:
        base_crit_dmg += .24

    # need to calculate avg crit power
    # this is a factor of laceration downtime
    # as a percentage of combat time
    # subtracted from max crit power

    # assume no randomness over 14 hits
    dmg_per_hit = dps

    crits_per_round = combat_time * (base_crit/100.0)  # where combat time is num hits
    crit_hit_dmg = dmg_per_hit * base_crit_dmg
    # builder dmg needs to be seperated from consumer (crit % will differ too...)
    crit_dmg = base_dmg * (base_crit / 100)
    print(crits_per_round)
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
