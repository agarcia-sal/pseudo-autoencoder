import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        logarithm_of_buckets = math.log(buckets)
        logarithm_of_states = math.log(states)
        pigs = math.ceil(logarithm_of_buckets / logarithm_of_states)
        return pigs