from typing import List

class BIT:
    def __init__(self, n: int):
        self.size = n
        self.tree = [0] * (n + 1)

    def update(self, idx: int, delta: int) -> None:
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def query(self, idx: int) -> int:
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)
        return result

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # pos[num] = index of num in nums1
        pos = [0] * n
        for i, num in enumerate(nums1):
            pos[num] = i

        # compressed[i] = position of nums2[i] in nums1
        compressed = [pos[num] for num in nums2]

        # Count elements smaller before i in compressed (using BIT)
        bit = BIT(n)
        smaller_count = [0] * n
        for i in range(n):
            idx = compressed[i]
            # query how many elements less or equal idx so far
            # Using idx as 0-based index, BIT is 1-based, so query idx
            # Smaller elements before i are those strictly less than idx
            # To get the count of elements smaller than idx, query(idx)
            # Since we want number of elements less than current idx 
            # and idx is 0-based, query idx gives count of elements with index < idx+1
            smaller_count[i] = bit.query(idx)
            bit.update(idx + 1, 1)

        # Count elements larger after i in compressed (using BIT)
        bit = BIT(n)
        larger_count = [0] * n
        for i in range(n - 1, -1, -1):
            idx = compressed[i]
            # number of elements with index > idx = total elements so far - number <= idx
            # total elements so far = bit.query(n)
            # number <= idx = bit.query(idx+1)
            # count larger after i =
            larger_count[i] = bit.query(n) - bit.query(idx + 1)
            bit.update(idx + 1, 1)

        good_triplets = 0
        for i in range(n):
            good_triplets += smaller_count[i] * larger_count[i]

        return good_triplets