from collections import defaultdict
from math import inf

class Solution:
    def maximumBeauty(self, flowers):
        indices = defaultdict(list)
        prefix_sum = [0] * (len(flowers) + 1)
        for i in range(len(flowers)):
            prefix_sum[i + 1] = prefix_sum[i] + max(flowers[i], 0)
            indices[flowers[i]].append(i)

        max_beauty = -inf
        for beauty in indices:
            if len(indices[beauty]) >= 2:
                first = indices[beauty][0]
                last = indices[beauty][-1]
                current_beauty = 2 * beauty + (prefix_sum[last] - prefix_sum[first + 1])
                if current_beauty > max_beauty:
                    max_beauty = current_beauty
        return max_beauty