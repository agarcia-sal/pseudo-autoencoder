class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def update(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result


class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos = [0] * n
        for i, num in enumerate(nums1):
            pos[num] = i

        compressed = [pos[num] for num in nums2]

        bit = BIT(n)
        smaller_count = [0] * n
        for i in range(n):
            smaller_count[i] = bit.query(compressed[i])
            bit.update(compressed[i] + 1, 1)

        bit = BIT(n)
        larger_count = [0] * n
        for i in reversed(range(n)):
            larger_count[i] = bit.query(n) - bit.query(compressed[i] + 1)
            bit.update(compressed[i] + 1, 1)

        good_triplets = 0
        for i in range(n):
            good_triplets += smaller_count[i] * larger_count[i]

        return good_triplets