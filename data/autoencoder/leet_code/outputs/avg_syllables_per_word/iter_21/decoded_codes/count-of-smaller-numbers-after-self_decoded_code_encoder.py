class Solution:
    def countSmaller(self, nums):
        sorted_nums = convert_set_to_sorted_list(nums)
        rank = create_rank_dictionary(sorted_nums)
        bit = initialize_bit(len(sorted_nums) + 1)

        def get_sum(idx):
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & -idx
            return res

        def update(idx, delta):
            while idx < len(bit):
                bit[idx] += delta
                idx += idx & -idx

        counts = []
        for num in reversed(nums):
            r = rank[num]
            counts.append(get_sum(r - 1))
            update(r, 1)

        result = counts[::-1]
        return result


def convert_set_to_sorted_list(collection):
    return sorted(set(collection))


def create_rank_dictionary(sorted_list):
    dictionary = {}
    for idx, val in enumerate(sorted_list):
        dictionary[val] = idx + 1
    return dictionary


def initialize_bit(size):
    return [0] * size