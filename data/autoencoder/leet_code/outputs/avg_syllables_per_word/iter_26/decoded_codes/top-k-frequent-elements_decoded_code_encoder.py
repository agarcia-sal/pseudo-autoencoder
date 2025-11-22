from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)
        for number in nums:
            frequency_map[number] += 1

        max_frequency = max(frequency_map.values(), default=0)
        buckets = [[] for _ in range(max_frequency + 1)]

        for number, frequency in frequency_map.items():
            buckets[frequency].append(number)

        result = []
        for frequency in range(max_frequency, 0, -1):
            if buckets[frequency]:
                result.extend(buckets[frequency])
                if len(result) >= k:
                    return result[:k]

        return result