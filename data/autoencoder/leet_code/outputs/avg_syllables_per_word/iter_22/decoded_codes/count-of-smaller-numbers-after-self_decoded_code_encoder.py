class Solution:
    def countSmaller(self, nums):
        sorted_nums = sorted(set(nums))
        rank = {num: i + 1 for i, num in enumerate(sorted_nums)}
        bit = [0] * (len(sorted_nums) + 1)

        def get_sum(idx):
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & (-idx)
            return res

        def update(idx, delta):
            while idx < len(bit):
                bit[idx] += delta
                idx += idx & (-idx)

        counts = []
        for num in reversed(nums):
            r = rank[num]
            counts.append(get_sum(r - 1))
            update(r, 1)

        return counts[::-1]