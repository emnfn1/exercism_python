EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    :param int elapsed_bake_time: Minutes the lasagna has already baked.
    :return: Remaining minutes the lasagna needs to bake.
    :rtype: int
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Each layer takes PREPARATION_TIME minutes to prepare.

    :param int number_of_layers: Number of lasagna layers prepared.
    :return: Total preparation time in minutes.
    :rtype: int
    """
    return number_of_layers * PREPARATION_TIME
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time in minutes.

    Elapsed time includes preparation time plus the time already spent baking.

    :param int number_of_layers: Number of lasagna layers prepared.
    :param int elapsed_bake_time: Minutes the lasagna*"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
