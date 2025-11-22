from math import inf

class Solution:
    def minimumIncompatibility(self, nums, k):
        total_length = len(nums)
        subset_size = total_length // k

        def count_occurrences(collection):
            count_map = {}
            for element in collection:
                count_map[element] = count_map.get(element, 0) + 1
            return count_map

        occurrences = count_occurrences(nums)
        for value in occurrences.values():
            if value > k:
                return -1

        subset_incompatibility = {}

        def count_bits(number):
            count = 0
            while number > 0:
                count += number & 1
                number >>= 1
            return count

        for mask in range(1 << total_length):
            if count_bits(mask) == subset_size:
                elements = []
                for index in range(total_length):
                    if (mask >> index) & 1:
                        elements.append(nums[index])

                def elements_are_unique(lst):
                    seen = set()
                    for item in lst:
                        if item in seen:
                            return False
                        seen.add(item)
                    return True

                if elements_are_unique(elements):
                    max_element = max(elements)
                    min_element = min(elements)
                    incompatibility_value = max_element - min_element
                    subset_incompatibility[mask] = incompatibility_value

        dp = [inf] * (1 << total_length)
        dp[0] = 0

        def bitwise_and(a, b):
            return a & b

        def bitwise_xor(a, b):
            return a ^ b

        for mask in range(1 << total_length):
            if count_bits(mask) % subset_size != 0:
                continue
            for subset_mask in subset_incompatibility:
                if bitwise_and(mask, subset_mask) == subset_mask:
                    candidate = dp[bitwise_xor(mask, subset_mask)] + subset_incompatibility[subset_mask]
                    if candidate < dp[mask]:
                        dp[mask] = candidate

        return -1 if dp[(1 << total_length) - 1] == inf else dp[(1 << total_length) - 1]