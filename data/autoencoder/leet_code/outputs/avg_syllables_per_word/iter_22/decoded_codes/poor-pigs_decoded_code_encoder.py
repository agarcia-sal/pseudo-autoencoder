import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        number_of_states = minutesToTest // minutesToDie + 1
        logarithm_of_buckets = math.log(buckets)
        logarithm_of_states = math.log(number_of_states)
        minimum_number_of_pigs = math.ceil(logarithm_of_buckets / logarithm_of_states)
        return minimum_number_of_pigs