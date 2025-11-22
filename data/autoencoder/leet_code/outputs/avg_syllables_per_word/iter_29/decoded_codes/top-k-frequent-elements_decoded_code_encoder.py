from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1

        max_frequency = max(frequency_map.values()) if frequency_map else 0
        buckets = [[] for _ in range(max_frequency + 1)]

        for num, freq in frequency_map.items():
            buckets[freq].append(num)

        result = []
        for freq in range(max_frequency, 0, -1):
            if buckets[freq]:
                result.extend(buckets[freq])
                if len(result) >= k:
                    return result[:k]
        return result