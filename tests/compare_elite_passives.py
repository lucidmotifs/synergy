# Script to determine optimal damage output for procs
# Initially crit and pen % will have to be manually entered.
# In future, hopefully this module can be used with just crit/pen glyph
# points (plus minor crit / major crit chance)

import formulae.damage

# This test is to see whether more damage is gained
# from which elite passive.
def test_compare_elite_passives(abilityList, player = Player()):
    ## Set All variables @TODO make external variables
    # test variables  @TODO make part of test object
    COMBAT_TIME = 30
    CRIT_CHANCE = 20  # set to a number to default back to
    CRIT_POWER = 40

    for a in abilityList:

        print("Testing with: {0}".format(a))
        # Create player object
        player.abilities.add(PassiveAbility(a))

        # Calculate theoretical base DPS
        # ...No procs or bleeds?
        base_dps = player.base_tdps()
        base_damage = player.base_tdps() * COMBAT_TIME

        if player.stats:
            crit_chance = player.stats.crit
            crit_power = player.stats.crit_power
        else:
            crit_chance = CRIT_CHANCE
            crit_power = CRIT_POWER
            # if player stats aren't initialized we have to add
            # extra crit chance from rapid getaway
            if a == "Rapid Getaway":
                crit_chance += 10

        if player.signets and player.signets("laceration"):
            v = data.items( "signet",
                            "laceration",
                            player.signets("laceration").quality)

            #uptime = formulae.buffs.laceration_uptime(player)
            uptime = 1  # assume for the moment @TODO create laceration_uptime

            crit_power += (v * uptime)

        # the below assumes one hit = one sec. Not always true
        # @TODO adjust below to account for multi hit attacks (use furmulae)
        total_crits = COMBAT_TIME * (crit_chance/100.0)
        # @TODO replace below with damage formulae
        total_crit_damage = base_damage * ((crit_chance/100.0) * crit_power)

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
