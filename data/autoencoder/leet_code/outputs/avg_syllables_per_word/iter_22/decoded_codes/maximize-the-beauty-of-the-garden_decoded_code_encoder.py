from collections import defaultdict
from math import inf

class Solution:
    def maximumBeauty(self, flowers):
        indices = defaultdict(list)
        n = len(flowers)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + max(flowers[i], 0)
            indices[flowers[i]].append(i)

        max_beauty = -inf
        for beauty, positions in indices.items():
            if len(positions) >= 2:
                first = positions[0]
                last = positions[-1]
                current_beauty = 2 * beauty + prefix_sum[last] - prefix_sum[first + 1]
                if current_beauty > max_beauty:
                    max_beauty = current_beauty

        return max_beauty