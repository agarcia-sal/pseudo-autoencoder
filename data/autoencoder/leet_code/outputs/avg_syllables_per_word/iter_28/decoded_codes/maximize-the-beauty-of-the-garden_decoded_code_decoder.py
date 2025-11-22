from collections import defaultdict
from math import inf
from typing import List

class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        indices = defaultdict(list)
        prefix_sum = [0] * (len(flowers) + 1)

        for i, val in enumerate(flowers):
            prefix_sum[i + 1] = prefix_sum[i] + max(val, 0)
            indices[val].append(i)

        max_beauty = -inf
        for beauty, positions in indices.items():
            if len(positions) >= 2:
                first = positions[0]
                last = positions[-1]
                current_beauty = 2 * beauty + prefix_sum[last] - prefix_sum[first + 1]
                if current_beauty > max_beauty:
                    max_beauty = current_beauty

        return max_beauty