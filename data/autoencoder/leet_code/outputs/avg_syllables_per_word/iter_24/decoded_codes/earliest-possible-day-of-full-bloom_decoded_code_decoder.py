from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        tasks = list(zip(plantTime, growTime))
        tasks.sort(key=lambda x: x[1], reverse=True)

        current_day = 0
        earliest_bloom = 0
        for plant_time, grow_time in tasks:
            current_day += plant_time
            bloom_day = current_day + grow_time
            if bloom_day > earliest_bloom:
                earliest_bloom = bloom_day
        return earliest_bloom