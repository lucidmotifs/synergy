# Define proc damage. Should be related to Attack Power - TODO find formula
class PROCS:
    ONE_IN_THE_CHAMBER = 264
    SUDDEN_RETURN = 264
    THUNDERSTRUCK = 392

def combat_round_average_hit(builder, priConsumer, secConsumer):
    # Calculate avg damage per hit
    # Below values are at 2800 AR / 446 WP
    builder = 214 # forumale.damage.builder_aoe
    consumer1 = 757 # formulae.damage.consumer_aoe_special
    consumer2 = 1511 # formulae.damage.consumer_special

    # 5 builders then each consumer used. This doesn't take into
    # account special attributes of consumers...
    ret = ((builder * 5) + consumer1 + consumer2) / 7

    return ret
