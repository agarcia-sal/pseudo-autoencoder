from collections import defaultdict
from typing import List

class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        indices = defaultdict(list)
        n = len(flowers)
        prefix_sum = [0] * (n + 1)

        # Build prefix sum of max(flowers[i], 0) and track indices of each beauty value
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + max(flowers[i], 0)
            indices[flowers[i]].append(i)

        max_beauty = float('-inf')
        for beauty, positions in indices.items():
            if len(positions) >= 2:
                first = positions[0]
                last = positions[-1]
                # Calculate current beauty as per formula:
                # 2 * beauty + prefix_sum[last] - prefix_sum[first + 1]
                current_beauty = 2 * beauty + prefix_sum[last] - prefix_sum[first + 1]
                if current_beauty > max_beauty:
                    max_beauty = current_beauty

        return max_beauty