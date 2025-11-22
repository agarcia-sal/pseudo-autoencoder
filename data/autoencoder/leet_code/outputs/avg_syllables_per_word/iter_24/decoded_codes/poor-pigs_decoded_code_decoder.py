import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        number_of_states = minutesToTest // minutesToDie + 1
        number_of_pigs = math.ceil(math.log(buckets, number_of_states))
        return number_of_pigs