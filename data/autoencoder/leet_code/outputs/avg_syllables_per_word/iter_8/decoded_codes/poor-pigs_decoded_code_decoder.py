import math

class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        states = minutesToTest // minutesToDie + 1
        pigs = math.ceil(math.log(buckets) / math.log(states))
        return pigs