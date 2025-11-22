class Solution:
    def countSmaller(self, nums):
        sorted_nums = sorted(set(nums))
        rank = {}
        index = 0
        for value in sorted_nums:
            index += 1
            rank[value] = index

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

        counts.reverse()
        return counts