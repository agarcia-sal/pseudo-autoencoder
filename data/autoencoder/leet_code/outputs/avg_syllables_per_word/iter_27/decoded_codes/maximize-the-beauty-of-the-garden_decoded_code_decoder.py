from collections import defaultdict
from typing import List

class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        indices = defaultdict(list)
        n = len(flowers)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + max(flowers[i], 0)
            indices[flowers[i]].append(i)

        max_beauty = float('-inf')
        for beauty_value, idx_list in indices.items():
            if len(idx_list) >= 2:
                first = idx_list[0]
                last = idx_list[-1]
                current_beauty = 2 * beauty_value + prefix_sum[last + 1] - prefix_sum[first + 1]
                if current_beauty > max_beauty:
                    max_beauty = current_beauty

        return max_beauty