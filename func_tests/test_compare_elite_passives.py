# Script to determine optimal damage output for procs
# Initially crit and pen % will have to be manually entered.
# In future, hopefully this module can be used with just crit/pen glyph
# points (plus minor crit / major crit chance)

# import modules
import data
import game.abilities
import game.formulae.damage

# TODO learn how to do Python module correctly to avoid this long hierarchy list
# import classes
from game.player import Player
from game.player import Stats


# This test is to see whether more damage is gained
# from which elite passive.
def run(alist, player = Player()):
    # Build wheel. This should be auto-matic when synergy starts, so
    # potentially global?
    wheel = game.abilities.AbilityList()

    # populate this ability list with everything
    wheel.populate(data.load())

    # debugging; checking wheel
    #print (wheel)

    # Test (remove to actual wheel creation test later...)
    if len(wheel.actives) == 0:
        print("Empty Wheel")
        return 0  # fail

    ## Set All variables @TODO make external variables
    # test variables  @TODO make part of test object
    COMBAT_TIME = 30
    CRIT_CHANCE = 20  # set to a number to default back to
    CRIT_POWER = 40

    for a in alist:
        # Load ability from wheel
        elitePassive = wheel.get(a)

        # Fail if we don't retrieve the ability
        if elitePassive is None:
            # throw TestFailException
            print("Test Failed: Could not retrieve ability from wheel [%s]\n"
                % a)
            return 0

        print("Testing with: {0}".format(elitePassive.name))

        # Create player object and add the elitePassive - this will replace
        # any other elite passive as there can only be one.
        player.deck().add(elitePassive)

        # Calculate theoretical base DPS
        # ...No procs or bleeds?
        base_dps = player.base_tdps()
        base_damage = player.base_tdps() * COMBAT_TIME

        if player.stats() is not None:
            crit_chance = player.stats().crit
            crit_power = player.stats().crit_power
        else:
            crit_chance = CRIT_CHANCE
            crit_power = CRIT_POWER
            # if player stats aren't initialized we have to add
            # extra crit chance from rapid getaway
            if a == "Rapid Getaway":
                crit_chance += 10

        if player.signets() and player.signets("laceration"):
            v = data.items( "signet",
                            "laceration",
                            player.signets("laceration").quality)

            #uptime = formulae.buffs.laceration_uptime(player)
            uptime = 1  # assume for the moment @TODO create laceration_uptime

            crit_power += (v * uptime)

        # the below assumes one hit = one sec. Not always true
        # @TODO adjust below to account for multi hit attacks (use furmulae)
        total_crits = COMBAT_TIME * (crit_chance/100)
        # @TODO replace below with damage formulae
        total_crit_damage = base_damage * ((crit_chance/100.0) * crit_power)

        # @TODO all proc damage calculation should be done in a formulae
        # subroutine:
        # game.formulae.proc_damage_per_crit(player)
        # would work something like -
        # if (passive)ability.requires()["attack"]["critical"]
        # and provide()["damage"]
        # add to AbilityList
        # check each item in list against player Deck, keep only
        # those that exist
        proc_dmg_per_crit = 0
        if player.using_ability("One in the Chamber"):
            proc_dmg_per_crit = PROCS.ONE_IN_THE_CHAMBER
        if player.using_ability("Thunderstruck"):
            proc_dmg_per_crit = int(wheel.get("Thunderstruck").provides["damage"]["amount"])

        total_proc_damage = proc_dmg_per_crit * int(total_crits)

        print("Base Damage: %d \n" % base_damage)
        print("Crit Damage: {0} ({1}% Crit) \n".format(int(total_crit_damage), crit_chance))
        print("Proc Damage: %d \n" % total_proc_damage)

        # end loop

    return 1
