import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        pigs = math.ceil(math.log(buckets, states))
        return pigs