import math

def poor_pigs(buckets, minutesToDie, minutesToTest):
    states = (minutesToTest // minutesToDie) + 1
    pigs = math.ceil(math.log(buckets) / math.log(states))
    return pigs