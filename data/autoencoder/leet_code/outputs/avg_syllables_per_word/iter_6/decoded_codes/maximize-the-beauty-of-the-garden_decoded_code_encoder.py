from collections import defaultdict

class Solution:
    def maximumBeauty(self, flowers):
        indices = defaultdict(list)
        prefix_sum = [0] * (len(flowers) + 1)

        for i, val in enumerate(flowers):
            prefix_sum[i + 1] = prefix_sum[i] + max(val, 0)
            indices[val].append(i)

        max_beauty = float('-inf')
        for beauty, positions in indices.items():
            if len(positions) >= 2:
                first, last = positions[0], positions[-1]
                current_beauty = 2 * beauty + prefix_sum[last] - prefix_sum[first + 1]
                if current_beauty > max_beauty:
                    max_beauty = current_beauty

        return max_beauty